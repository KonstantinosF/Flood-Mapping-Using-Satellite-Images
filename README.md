# Flood-Mapping-Using-Satellite-Images
MSc Thesis - Data Science - UoP &amp; NCSR "Demokritos"

The dataset used is named as <b>Sen1Floods11</b> and it is comprised with Sentinel 1 & 2 images with the corresponding ground truth masks. The dataset contains two main folders (<b>flood_events & perm_water</b>) as shown below:

![Capture](https://user-images.githubusercontent.com/23013328/156328362-d9ed2228-bd20-4d75-b254-711b1da30d08.PNG)

The <b>flood_events</b> folder is further splitted into 2 subfolders as shown in the image below:

![image](https://user-images.githubusercontent.com/23013328/159184483-b63def56-2d9c-46c4-9920-2439ee44d705.png)

The <b> HandLabeled </b> subfolder is splitted into 6 subfolders as shown in the image below:

![Capture2](https://user-images.githubusercontent.com/23013328/156328879-6268e602-c81c-4275-8ae4-7d4085baf820.PNG)

While the <b>WeaklyLabeled</b> folder

![image](https://user-images.githubusercontent.com/23013328/158182582-fd4a76e3-9842-4221-a285-e02dcad35e28.png)


<h2> Flood Events </h2>

<h3> Hand Labeled </h3> 
This subfolder contains one folder <b> S1Hand</b> which consists of sentinel 1 image patches with two polarization bands (VH & VV) and another one called <b> S2Hand </b> which includes Sentinel 2 image patches with all 13 spectral bands. The rest folders are the coresponding ground trouth mask, each one being created with a different method. The areas of study are 12 countries as shown below:

![Screenshot 2022-03-01 at 22 29 28](https://user-images.githubusercontent.com/23013328/156243983-dd862316-9998-4c27-91ea-600603a84e4b.png)


<h3> Weakly Labeled </h3>


![Screenshot 2022-03-01 at 22 28 50](https://user-images.githubusercontent.com/23013328/156243919-c9205e31-730b-42f1-ab17-27a27661b341.png)


<h2> Experiments  </h2>

<h3>1. U-NET </h3>
<p align="center">

U-Net is a convolutional neural network that was developed for biomedical image segmentation. The network is based on the <b>fully convolutional network</b> and its architecture was modified and extended to work with fewer training images and to yield more precise segmentations. The network consists of a contracting path (convolution) and an expansive path (deconvolution), which gives it the u-shaped architecture. The contracting path is a typical convolutional network that consists of repeated application of convolutions, each followed by a rectified linear unit (ReLU) and a max pooling operation. During the contraction, the spatial information is reduced while feature information is increased. The expansive pathway combines the feature and spatial information through a sequence of up-convolutions and concatenations with high-resolution features from the contracting path. [https://en.wikipedia.org/wiki/U-Net#cite_note-Shelhamer_2017-2]
</p>

![image](https://user-images.githubusercontent.com/23013328/159357537-8c5fff43-910e-4ce1-a98b-773b7836a0b8.png)


| Source & Labels          | Test Accuracy |  IoU |
| ------------------------ |   ----------- | ---- |
| S1Hand & LabelHand       |     78.25     |      |
| S1Hand & S1OtsuLabelHand |     88.4      |      |
| S1Hand & JRCWaterHand    |     96.28     |      |
| S2Hand & JRCWaterHand    |     96.50     | 0.48 |
| S2Hand & LabelHand       |     75.60     |      |



<h3> 2. XNet </h3>

<h3> 3. Transfer Learning - VGG16 </h3>

<h2> Pre - Processing - Sentinel 1 </h2>

- Apply orbit file 
- GRD border noise removal
- Thermal noise removal
- Radiometric calibration
- Terrain correction (orthorectification)
  
