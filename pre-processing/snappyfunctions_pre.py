from osgeo import ogr
import imageio
import matplotlib.pyplot as plt
import numpy as np
# import rasterio

import snappy
from os.path import join
from glob import glob
import numpy as np
import os
import glob
import jpy
System = jpy.get_type('java.lang.System')
System.gc()
import gc

import re
from geomet import wkt
from snappy import GPF
from snappy import ProductIO
from snappy import HashMap
from snappy import jpy
HashMap = snappy.jpy.get_type('java.util.HashMap')
import time

from osgeo import gdal, ogr
import sys
from osgeo import osr

import configparser
from os.path import expanduser
os.chdir(r"D:\MICROS\Ship_detection")



def subset(image):
    
    region =  'POLYGON ((33.0130819325524 34.54982297667559, 33.285059184082606 34.58857638473086, 33.25449505627861 34.734151031006526, 32.98203732050098 34.6954232998211,33.0130819325524 34.54982297667559))'
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    parameters = snappy.HashMap()
    parameters.put('copyMetadata', True)
    parameters.put('geoRegion', region)

    subset = snappy.GPF.createProduct('Subset', parameters, image)
    parameters = None
    print('Subset implemented succesfully...')
    
    
    return subset



def importvector(image):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    #shape = fiona.open('C:\\Users\\Kostas-Geosystems\\Desktop\\Ship_detection\\AOI\\Cyprus_Coastline_Final_V2\\Cyprus_Coastline_Final_V2.shp')
    shape_path = r'D:\\MICROS\\Ship_detection\\Cyprus_Coastline_Final_V2.shp'
    shapef = "D:/MICROS/Ship_detection/AOI/Cyprus_Coastline_Final_V2/Cyprus_Coastline_Final_V2.shp"
    
    parameters = HashMap()
    parameters.put('vectorFile', shapef)
    parameters.put('separateShapes', True)
    
    addvector = snappy.GPF.createProduct('Import-Vector', parameters, image)
    parameters = None
    print('The land mask added succesfully...')
    
    return addvector


def landmask(image):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    parameters = snappy.HashMap()
    parameters.put('sourceBands', 'Intensity_VH')
    parameters.put('landMask', False)
    parameters.put('useSRTM', False)
    parameters.put('geometry', 'Cyprus_Coastline_Final_V2_1')
    parameters.put('invertGeometry', True)
    parameters.put('shorelineExtension', 35)
    #parameters.put('byPass', False)
    
    maskland = snappy.GPF.createProduct('Land-Sea-Mask', parameters, image)
    parameters = None
    print('The land mask added succesfully...')
    
    return maskland

def calibration(image):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    parameters = snappy.HashMap()
    parameters.put('sourceBands', 'Intensity_VH')
    parameters.put('outputImageScaleInDb', True)

    calibrated = snappy.GPF.createProduct('Calibration', parameters, image)
    parameters = None
    print('Calibration implemented succesfully...')
    
    return calibrated

def adaptivethresholding(image):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    
    parameters = snappy.HashMap()
    parameters.put('targetWindowSizeInMeter', 250)
    parameters.put('guardWindowSizeInMeter', 600.0)
    parameters.put('backgroundWindowSizeInMeter', 800.0)
    parameters.put('pfa', 16.0)
    parameters.put('estimateBackground', False)

    threshold = snappy.GPF.createProduct('AdaptiveThresholding', parameters, image)
    parameters = None
    print('Adaptive Thresholding implemented succesfully...')
    
    return threshold

def objectdiscrimination(image):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    parameters = snappy.HashMap()
    parameters.put('minTargetSizeInMeter', 30.0)
    parameters.put('maxTargetSizeInMeter', 800.0)
    
    objectdetection = snappy.GPF.createProduct('Object-Discrimination', parameters, image)
    parameters = None
    print('Object Discimination implemented succesfully...')
    
    return objectdetection

def applyorbitfile(image):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')

    parameters = snappy.HashMap()
    parameters.put('orbitType', 'Sentinel Precise (Auto Download)')
    parameters.put('continueOnFail', True)

    orbit_correction = snappy.GPF.createProduct('Apply-Orbit-File', parameters, image)
    parameters = None
    print('Apply Orbit File implemented succesfully...')
    
    return orbit_correction


def terraincorrection(image):
    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')
    
    proj = '''GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.0174532925199433,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]'''

    parameters = snappy.HashMap()
    parameters.put('demName', 'SRTM 1Sec HGT')
    parameters.put('sourceBands', 'Sigma0_VH')
    parameters.put('imageResamplingMethod', 'BILINEAR_INTERPOLATION')
    parameters.put('pixelSpacingInMeter', 10.0)
    parameters.put('mapProjection', proj)
    parameters.put('noDataValueAtSea', False)
    parameters.put('saveSelectedSourceBand', True)
    parameters.put('nodataValueAtSea', False)

    terrain_correction = snappy.GPF.createProduct('Terrain-Correction', parameters, image)
    parameters = None
    print('Terrain Correction implemented succesfully...')
    
    return terrain_correction





