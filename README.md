# Flood-Mapping-Using-Satellite-Images
MSc Thesis - Data Science - UoP &amp; NCSR "Demokritos"

The dataset used is named as <b>Sen1Floods11</b> and it is comprised with Sentinel 1 & 2 images with the corresponding ground truth masks. The dataset contains two main folders (<b>flood_events & perm_water</b>) as shown below:

![Capture](https://user-images.githubusercontent.com/23013328/156328362-d9ed2228-bd20-4d75-b254-711b1da30d08.PNG)

The <b>flood_events</b> folder is further splitted into 2 subfolders as shown in the image below:

![image](https://user-images.githubusercontent.com/23013328/159184483-b63def56-2d9c-46c4-9920-2439ee44d705.png)

The <b> HandLabeled </b> subfolder is splitted into 6 subfolders as shown in the image below:

![Capture2](https://user-images.githubusercontent.com/23013328/156328879-6268e602-c81c-4275-8ae4-7d4085baf820.PNG)

While the <b>WeaklyLabeled</b> folder is splitted into 3.

![image](https://user-images.githubusercontent.com/23013328/158182582-fd4a76e3-9842-4221-a285-e02dcad35e28.png)


<h2> Flood Events </h2>

<h3> Hand Labeled </h3> 
This subfolder contains one folder <b> S1Hand</b> which consists of sentinel 1 image patches with two polarization bands (VH & VV) and another one called <b> S2Hand </b> which includes Sentinel 2 image patches with all <b>13 spectral bands</b>. It should be noticed that not all bands share the same spatial resolution, thus if needed an extra processing (pansharpening) should be applied. The size of the patches is 512x512 within the coordinate system EPSG:4326 - WGS 84 - Geographic. The rest folders are the coresponding ground trouth mask, each one being created with a different method. The areas of study are parts of 12 countries as shown below:

![Screenshot 2022-03-01 at 22 29 28](https://user-images.githubusercontent.com/23013328/156243983-dd862316-9998-4c27-91ea-600603a84e4b.png)


<h3> Weakly Labeled </h3>


![Screenshot 2022-03-01 at 22 28 50](https://user-images.githubusercontent.com/23013328/156243919-c9205e31-730b-42f1-ab17-27a27661b341.png)


<h2> Experiments  </h2>

<h3>1. U-NET </h3>
<p align="center">

U-Net is a convolutional neural network that was developed for biomedical image segmentation. The network is based on the <b>fully convolutional network</b> and its architecture was modified and extended to work with fewer training images and to yield more precise segmentations. The network consists of a contracting path (convolution) and an expansive path (deconvolution), which gives it the u-shaped architecture. The contracting path is a typical convolutional network that consists of repeated application of convolutions, each followed by a rectified linear unit (ReLU) and a max pooling operation. During the contraction, the spatial information is reduced while feature information is increased. The expansive pathway combines the feature and spatial information through a sequence of up-convolutions and concatenations with high-resolution features from the contracting path. [https://en.wikipedia.org/wiki/U-Net#cite_note-Shelhamer_2017-2]
</p>

![image](https://user-images.githubusercontent.com/23013328/159357537-8c5fff43-910e-4ce1-a98b-773b7836a0b8.png)

| Hand Labeled             |               |      | Weakly Labeled          |               |     | Weakly Supervised       |               |     |
| ------------------------ | ------------- | ---- | ----------------------- | ------------- | --- | ----------------------- | ------------- | --- |
| Source & Labels          | Test Accuracy |  IoU | Source & Labels         | Test Accuracy | IOU | Trained On              | Tested on     | IOU |
| ------------------------ |  ------------ | ---- | ----------------------- | ------------- | --- | ----------------------- | ------------- | --- |
| S1Hand & LabelHand       |     78.25     | 0.38 | S1Weak & S1OtsuLabelWeak|    81.72      |40.86| S1Hand & S1OtsuLabelWeak| LabelHand     |     |
| S1Hand & S1OtsuLabelHand |     88.4      | 0.38 | S1Weak & S2IndexLabelWea|    79.08      |39.54| S1Hand & S2IndexLabel   | LabelHand     |     |
| S1Hand & JRCWaterHand    |     96.28     | 0.48 |                         |               |     |                         |               |     |
| S2Hand & JRCWaterHand    |     96.50     | 0.48 |                         |               |     |                         |               |     |
| S2Hand & LabelHand       |     75.60     | 0.38 |                         |               |     |                         |               |     |
| S2Hand & S1OtsuLabelHand |     90.08     | 0.45 |                         |               |     |                         |               |     |

S2Hand & LabelHand = Test Loss ->58.17374587059021
S2Hand & S1OtsuLabelHand = Test Loss ->36.47
S1Weak & S1OtsuLabelWeak = Test Loss-> 55.919 (444 samples , equaly from all classes, 37 samples per class)
S1Weak & S2IndexLabelWea = Test Loss-> 51.810 (444 samples , equaly from all classes, 37 samples per class)

<h3> 2. Random Forest - Feature Engineering </h3>
Feature based segmentation using Random Forest

List of Hand Crafted Features:
  
- <b> Roberts Cross </b> </br>
  <p> The Roberts cross operator is used for edge detection. As a differential operator, the idea behind the Roberts cross operator is to approximate the       gradient of an image through discrete differentiation which is achieved by computing the sum of the squares of the differences between diagonally         adjacent pixels. </p>
- <b> Median </b> </br>
   The median filter is a non-linear digital filtering technique, often used to remove noise from an image or signal. Median filtering is widely used in      digital image processing because it preserves edges while removing noise.
- <b> Variance </b> </br>
- <b> NDVI </b> </br>
The Normalized Difference Vegetation Index (NDVI) was created with the aim of separating vegetation from soil brightness using Landsat MSS satellite data. Among the advantages of the index is the minimization of topographical effects. It is also almost invariant to different conditions because of the normalized values. The range of values ​​is from -1 to +1 with 0 expressing the absence of vegetation while negative values ​​describe land covers such as water, man-made structures, etc. More specifically, values close to zero (-0.1 to 0.1) generally correspond to barren areas of rock, sand, or snow. Low, positive values represent shrub and grassland (approximately 0.2 to 0.4), while high values indicate temperate and tropical rainforests (values approaching 1). The disadvantages of the index are that it shows saturation at very high concentrations of vegetation and overestimation at low vegetation concentrations due to soil reflectivity. Finally, atmospheric conditions, such as thin clouds, can potentially affect NDVI values.

The formula for retrieving NDVI values is the following:

NDVI = (NIR - RED) / (NIR + RED)

More specifically for Sentinel 2 band the formula is modified as follows:

- <b> MNDWI </b> </br>
The Modified Normalized Difference Water Index (MNDWI) uses green and SWIR bands for the enhancement of open water features. It also diminishes built-up area features that are often correlated with open water in other indices. The modified NDWI (MNDWI) can enhance open water features while efficiently suppressing and even removing built‐up land noise as well as vegetation and soil noise. The enhanced water information using the NDWI is often mixed with built‐up land noise and the area of extracted water is thus overestimated. Accordingly, the MNDWI is more suitable for enhancing and extracting water information for a water region with a background dominated by built‐up land areas.
    The MNDWI results from the following equation:
          MNDWI = (Green - SWIR) / (Green + SWIR)
    More specifically for Sentinel 2 bands the MNDWI the equation is formed as follows:

    MNDWI = (B3 - B11) / (B3 + B11)



| Hand Labeled             |               |      | Weakly Labeled          |               |     | Weakly Supervised       |               |     |
| ------------------------ | ------------- | ---- | ----------------------- | ------------- |---- | ----------------------- | ------------- | --- |
| Source & Labels          | Test Accuracy |  IoU | Source & Labels         | Test Accuracy | IOU | Trained On              | Tested on     | IOU |
| ------------------------ |   ----------- | ---- | ----------------------- | ------------- | --- | ----------------------- | ------------- | --- |
| S1Hand & LabelHand       |   0.924       | 0.144| S1Weak & S1OtsuLabelWeak|               |     | S1Hand & S1OtsuLabelWeak| LabelHand     |     |
| S1Hand & S1OtsuLabelHand |   0.89        |0.1508| S1Weak & S2IndexLabelWea|               |     | S1Hand & S2IndexLabel   | LabelHand     |     |
| S1Hand & JRCWaterHand    |   0.990       |0.1044|                         |               |     |
| S2Hand & JRCWaterHand    |   0.9898      |0.0636|                         |               |     |
| S2Hand & LabelHand       | 0.93          |0.15  |                         |               |     |
| S2Hand & S1OtsuLabelHand | 0.9025        |0.1882|                         |               |     |

<h3> 3. Transfer Learning - VGG16 </h3>

![image](https://user-images.githubusercontent.com/23013328/166447610-df628514-8824-4641-8180-5eb4bd1c4e26.png)

A CNN can be divided into two main parts: Feature learning and classification.

Feature Learning

In this part, the main goal of the NN is to find patterns in the pixels of the images that can be useful to identify the targets of the classification. That happens in the convolution layers of the network that specializes in those patterns for the problem at hand.

Classification

Now we want to use those patterns to classify our images to their correct label. This part of the network does exactly that job, it uses the inputs from the previous layers to find the best class to your matched patterns in the new image.

| Hand Labeled             |               |      | Weakly Labeled          |               |     |
| ------------------------ | ------------- | ---- | ----------------------- | ------------- |---- |
| Source & Labels          | Test Accuracy |  IoU | Source & Labels         | Test Accuracy | IOU |
| ------------------------ |   ----------- | ---- | ----------------------- | ------------- | --- |
| S1Hand & LabelHand       |               |      | S1Hand & S1OtsuLabelWeak|               |     |
| S1Hand & S1OtsuLabelHand |               |      | S1Weak & S2IndexLabelWea|               |     |
| S1Hand & JRCWaterHand    |               |      |                         |               |     |
| S2Hand & JRCWaterHand    |               |      |                         |               |     |
| S2Hand & LabelHand       |               |      |                         |               |     |
| S2Hand & S1OtsuLabelHand |               |      |                         |               |     |


Reference: https://towardsdatascience.com/transfer-learning-with-vgg16-and-keras-50ea161580b4

<h2> Pre - Processing - Sentinel 1 </h2>

- Apply orbit file 
- GRD border noise removal
- Thermal noise removal
- Radiometric calibration
- Terrain correction (orthorectification)
  
