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

| Hand Labeled             |               |      |
| ------------------------ | ------------- | ---- |
| Source & Labels          | Test Accuracy |  IoU |
| ------------------------ |   ----------- | ---- |
| S1Hand & LabelHand       |     78.25     | 0.38 |
| S1Hand & S1OtsuLabelHand |     88.4      | 0.38 |
| S1Hand & JRCWaterHand    |     96.28     | 0.48 |
| S2Hand & JRCWaterHand    |     96.50     | 0.48 |
| S2Hand & LabelHand       |     75.60     | 0.38 |



<h3> 2. Random Forest - Feature Engineering </h3>
Feature based segmentation using Random Forest

List of Hand Crafted Features:

- <b> Gabor Filter </b> </br>
  <p> In image processing, a Gabor filter, is a linear filter used for texture analysis, which essentially means that it analyzes whether there is any           specific frequency content in the image in specific directions in a localized region around the point or region of analysis. </p>
  
- <b> Roberts Cross </b> </br>
  <p> The Roberts cross operator is used for edge detection. As a differential operator, the idea behind the Roberts cross operator is to approximate the       gradient of an image through discrete differentiation which is achieved by computing the sum of the squares of the differences between diagonally         adjacent pixels. </p>
- <b> SOBEL </b> </br>
 <p> The Roberts cross operator is used in image processing and computer vision for edge detection. It was one of the first edge detectors and was              initially proposed by Lawrence Roberts in 1963.[1] As a differential operator, the idea behind the Roberts cross operator is to approximate the            gradient of an image through discrete differentiation which is achieved by computing the sum of the squares of the differences between diagonally          adjacent pixels. </p>
- SCHARR
- PREWITT
- GAUSSIAN with sigma=3
- GAUSSIAN with sigma=7
- MEDIAN with sigma=3
- VARIANCE with size=3

<h3> 3. Transfer Learning - VGG16 </h3>

![image](https://user-images.githubusercontent.com/23013328/166447610-df628514-8824-4641-8180-5eb4bd1c4e26.png)

A CNN can be divided into two main parts: Feature learning and classification.

Feature Learning

In this part, the main goal of the NN is to find patterns in the pixels of the images that can be useful to identify the targets of the classification. That happens in the convolution layers of the network that specializes in those patterns for the problem at hand.

Classification

Now we want to use those patterns to classify our images to their correct label. This part of the network does exactly that job, it uses the inputs from the previous layers to find the best class to your matched patterns in the new image.




Reference: https://towardsdatascience.com/transfer-learning-with-vgg16-and-keras-50ea161580b4

<h2> Pre - Processing - Sentinel 1 </h2>

- Apply orbit file 
- GRD border noise removal
- Thermal noise removal
- Radiometric calibration
- Terrain correction (orthorectification)
  
