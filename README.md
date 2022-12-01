# Flood-Mapping-Using-Satellite-Images
MSc Thesis - Data Science - UoP &amp; NCSR "Demokritos"

<h2> Download The Dataset </h2>

- <b>First Option:</b><br>
    Visit the following link: <br>
    https://mlhub.earth/data/c2smsfloods_v1 (you need to create an account first)
  
- <b>Second Option:</b><br>
  The dataset is available for access through Google Cloud Storage bucket at: gs://senfloods11/

  You can access the dataset bucket using the gsutil command line tool. If you would like to download the entire dataset (~14 GB) you can use gsutil       rsync to clone the bucket to a local directory. The -m flag is recommended to speed downloads. The -r flag will download sub-directories and folder       recursively. See the example below.

  <i> $ gsutil -m rsync -r gs://sen1floods11 /YOUR/LOCAL/DIRECTORY/HERE </i>

<h2> Dataset Information </h2>

The dataset used is named as <b>Sen1Floods11</b> and it is comprised with Sentinel 1 & 2 images with the corresponding ground truth masks. The dataset contains two main folders (<b>flood_events & perm_water</b>) as shown below:

<p float="left">
  <img src="./imgs/Folder1.png" width="650" />
</p>

In this study we are only using the images included on the <b>Flooed Events</b> folder and eliminate the permanent water images. The <b>flood_events</b> folder is further splitted into 2 subfolders as shown in the image below:




The <b> HandLabeled </b> subfolder is splitted into 6 subfolders as shown in the image below:

![Capture2](https://user-images.githubusercontent.com/23013328/156328879-6268e602-c81c-4275-8ae4-7d4085baf820.PNG)

While the <b>WeaklyLabeled</b> folder is splitted into 3.

![image](https://user-images.githubusercontent.com/23013328/158182582-fd4a76e3-9842-4221-a285-e02dcad35e28.png)


<h2> Flood Events </h2>

<h3> Hand Labeled </h3> 
This subfolder contains one folder <b> S1Hand</b> which consists of sentinel 1 image patches with two polarization bands (VH & VV) and another one called <b> S2Hand </b> which includes Sentinel 2 image patches with all <b>13 spectral bands</b>. It should be noticed that not all bands share the same spatial resolution, thus if needed an extra processing (pansharpening) should be applied. The size of the patches is 512x512 within the coordinate system EPSG:4326 - WGS 84 - Geographic. The rest folders are the coresponding ground trouth mask, each one being created with a different method. The areas of study are parts of 12 countries as shown below:

<p float="left">
  <img src="./imgs/HandLabeledTable.png" width="500" />
</p>


<h3> Weakly Labeled </h3>

<p float="left">
  <img src="./imgs/WeaklyLabeledTable.png" width="500" />
</p>
As can be seen the size of the Weakly labeled dataset is much larger thant the hand labeled one.

<h2> Clean the Dataset - Pre Process </h2>

After visualy checking the dataset with manually loading several image patches on a free and open Geographic Information System software called <a href="https://www.qgis.org/en/site/">QGIS</a>, we noticed that many images do not contain pixels with flood. Additionally we saw that many sentinel 2 images are majored covered with clouds which makes them useless.

Bellow is an illustration of a sentinel 2 image tile blocked with clouds and the corresponding sentinel 1 tile and the label from it...of the same area.

<p float="left">
  <img src="./imgs/s2.png" width="200" />
  <img src="./imgs/s1.png" width="200" /> 
  <img src="./imgs/label.png" width="200" />
</p>

Additionaly some images are appeared to be acquired as "half" with this part of the image to be labeled as (-1) the same as the clouds.

<p float="left">
  <img src="./imgs/S2_half.png" width="200" />
  <img src="./imgs/Label_half.png" width="200" /> 
</p>

Furthermote in order to create a set of sentinel 2 and sentinel 1 datasets which will be comparable we decided to remove the image tiles with at least one pixel of clouds...Since sentinel 1 labels do not have the label -1 (clouds). ...to be able to create a multi-modal dataset. It was decided that the labeling dataset JRCWaterHand will not be used since it doesn't cover floods but permanent waters.

The initial image tiles of 512x512 size were splited into patches of 128x128. So from each itinial image 16 patches were created. In a google colab environment it took 8 to 10 hours to finish.

After spliting the intial images, we resulted into 7136 128x128 image patches for S1Hand,S2Hand, LabelHand and S1OtsuLabelHand. From these we identified the patches with only (-1) label and deleted them. After this proccess we ended up with 6825 patches.

Bolivia new: 231
Ghana new: 650
India new: 1068
Mekong new: 479
Nigeria new: 282
Pakistan new: 417
Paraguay new: 1055
Somalia new: 414
Spain new: 478
Sri-Lanka new: 663
USA new: 1088
![image](https://user-images.githubusercontent.com/23013328/203274402-ca9dcecc-fd6c-4255-b6cc-f9c39295b792.png)


The link for the new dataset: https://uopel-my.sharepoint.com/:f:/g/personal/dit2025dsc_office365_uop_gr/EomiPN1R1GNMuYLDtHBQgaoBVZ1GBJ-Xfo8xGmuSfAh2Ug?e=wKLRmL


<h2> Experiments  </h2>
Experiments were splited into three parts, with each one based on a different semantic segmentation scheme. The first one is based on a RAndom Forest architecture and a set of hand crafted features, the second is based on the concept of transfer learning while the last on is based on a U-NET fully convolutional neural network. 

<h3>0. MNDWI and Otsu Thresholding - Baseline model </h3>
<p align="center">

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
The Normalized Difference Vegetation Index (NDVI) was created with the aim of separating vegetation from soil brightness. The range of values ​​is from -1 to +1 with 0 expressing the absence of vegetation while negative values ​​describe land covers such as water, man-made structures, etc. More specifically, values close to zero (-0.1 to 0.1) generally correspond to barren areas of rock, sand, or snow. Low, positive values represent shrub and grassland (approximately 0.2 to 0.4), while high values indicate temperate and tropical rainforests (values approaching 1).

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
| S1Hand & LabelHand       |   0.924       | 0.144| S1Weak & S1OtsuLabelWeak| 0.8035        |     | S1Hand & S1OtsuLabelWeak| LabelHand     |     |
| S1Hand & S1OtsuLabelHand |   0.89        |0.1508| S1Weak & S2IndexLabelWea| 0.1520        |     | S1Hand & S2IndexLabel   | LabelHand     |     |
| S1Hand & JRCWaterHand    |   0.990       |0.1044|                         |               |     |
| S2Hand & JRCWaterHand    |   0.9898      |0.0636|                         |               |     |
| S2Hand & LabelHand       | 0.93          |0.15  |                         |               |     |
| S2Hand & S1OtsuLabelHand | 0.9025        |0.1882|                         |               |     |

## Multi-Modal

| Hand Labeled                        |               |      | Weakly Supervised                |               |     |
| ----------------------------------- | ------------- | ---- | -----------------------          | ------------- | --- |
| Source & Labels                     | Test Accuracy | IoU  | Trained On                       | Tested on     | IOU |
| ----------------------------------- |-------------- | ---- | -----------------------          | ------------- | --- |
| S1Hand - S2Hand & LabelHand         | 0.9374        |0.2987| S1Hand - S2Hand & S1OtsuLabelWeak| LabelHand     |     |
| S1Hand - S2Hand & S1OtsuLabelHand   |0.9010         |0.1784| S1Hand - S2Hand & S2IndexLabel.  |.              |.    |
| S1Hand - S2Hand & JRCWaterHand      |0.99255        |0.3239|


<h3> 3. Transfer Learning - VGG16 </h3>

![image](https://user-images.githubusercontent.com/23013328/166447610-df628514-8824-4641-8180-5eb4bd1c4e26.png)

A CNN can be divided into two main parts: Feature learning and classification.

Feature Learning

In this part, the main goal of the NN is to find patterns in the pixels of the images that can be useful to identify the targets of the classification. That happens in the convolution layers of the network that specializes in those patterns for the problem at hand.

Classification

Now we want to use those patterns to classify our images to their correct label. This part of the network does exactly that job, it uses the inputs from the previous layers to find the best class to your matched patterns in the new image.

| Hand Labeled             |               |      | Weakly Labeled          |               |     | Weakly Supervised       |               |     |
| ------------------------ | ------------- | ---- | ----------------------- | ------------- |---- | ----------------------- | ------------- | --- |
| Source & Labels          | Test Accuracy |  IoU | Source & Labels         | Test Accuracy | IOU | Trained On              | Tested on     | IOU |
| ------------------------ |   ----------- | ---- | ----------------------- | ------------- | --- | ----------------------- | ------------- | --- |
| S1Hand & LabelHand       |               |      | S1Hand & S1OtsuLabelWeak|               |     | S1Hand & S1OtsuLabelWeak| LabelHand     |     |
| S1Hand & S1OtsuLabelHand |               |      | S1Weak & S2IndexLabelWea|               |     | S1Hand & S2IndexLabel   | LabelHand     |     |
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
  
