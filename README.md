# Iris Segmentation

Segmentation is the process of finding most important portions in any image.  It is achieved by localizing the iris-pupil boundary, iris-sclera boundary, eyelids and eyelashes. Proper segmentation is essential for feature extraction and feature matching at later stages. We selected the CASIA Interval v4 dataset developed at the Centre for Biometrics and Security Research using near infrared (NIR) imagery. A sample iris image from the dataset is shown in Fig 1.

Thresholding is the simplest method for image segmentation. For this purpose, a grayscale image is used. If the intensity of a pixel I(x, y) is greater than a threshold, it is marked as white, otherwise it is marked black. Thresholding produces a binary image. On using this process on our iris image, we obtained the binary image shown in in Fig 2.

The image obtained in Fig 2 was further processed using a morphology technique called open. In this technique, erosion is done followed by dilation. The result obtained is shown in Fig 3.

We tried to detect contours in the image shown in Fig 3. Contours are curves joining continuous points along a boundary region. These can be points with same intensity or same colour. A binary image is usually used for contour detection. Of all the contours obtained, the outre mose contour was selected. These can be seen on Fig 4 and Fig 5.

![thresholding and hough circles](https://github.com/manujagobind/Iris/raw/master/Screenshots/Screenshot1.png)

With the help of this method, we were able to detect the iris-pupil circular boundary, its centre and radius. Unfortunately, this method did not help in detecting iris-sclera boundary due to low intensity difference between the two regions.

We also used local thresholding to see if iris-sclera regions were detected. The image was divided into 16 (4x4) parts and thresholding was applied independently on each. The result obtained is shown below (Fig 6).

![thresholding and hough circles](https://github.com/manujagobind/Iris/raw/master/Screenshots/Screenshot2.png)

Given a preprocessed image I(x, y), a Canny edge operator is applied to obtain a set of edge points. A voting procedure is employed to ascertain whether that edge point lies on a circular region or not. The voting procedure results a local maxima in the accumulator space, if the corresponding edge points in the image space lie on a circular region. The voting procedure is given as follows:

For all edge points (xi, yi) in the image space,
H(xc, yc, r) = ∑ h(xi, yi, xc, yc, r)
where
h(xi, yi, xc, yc, r) = 1,                if g(xi, yi, xc, yc, r) = 0
              h(xi, yi, xc, yc, r) = 0,                otherwise
and
g(xi, yi, xc, yc, r) = (xi – xc)2 + (yi – yc)2  - r2
Thus  h(xi, yi, xc, yc, r) = 1 if the parameter triplet (xc, yc, r) represents a circle passing through the edge point (xi, yi) The accumulator cell that gets maximum number of votes is considered most suitable to represent the circular contour.

We used the centre and radius obtained from Fig 5 as the minimum criteria for detecting circles. The maximum criteria for radius was set as twice the one obtained in Fig 5. The result obtained is shown below (Fig 7). The result obtained using OpenCV’s built in function was not upto the mark. A better algorithm for the same has to be used or self designed.

![thresholding and hough circles](https://github.com/manujagobind/Iris/raw/master/Screenshots/Screenshot1.png)

In an attempt to localize iris-sclera boundary, we used the method proposed in [2]. Saliency maps can be used to measure variation in contrast and thus provide sharp responses along the edges. However, the method did not prove to be very successful on the CASIA dataset as it did on the MICHE dataset. Although the pupil region was detected, the iris-sclera boundary went undetected. The reason maybe low intensity difference between iris and sclera regions. This is shown in Fig 8.

![thresholding and hough circles](https://github.com/manujagobind/Iris/raw/master/Screenshots/Screenshot1.png)

### FUTURE WORK:

The methods used in this research did not prove to be very successful in localizing the iris-sclera boundary. Future work involves improving or redesigning the algorithms already employed and reading and implementing other methods that could be used for iris segmentation. One such method  to test could be background subtraction. The algorithms should also be tested on various other iris datasets such as MICHE, VSSIRIS, OSIRIS, etc.
