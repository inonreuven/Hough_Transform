# Hough_Transform
Straight lines detection with Hough Transform using cv2 and scikit-learn.  

## Contents
1. Objective
  1.1 Hough transform 
2. Requirments 
3. Data 


## 1. Objective
This project aims to:
1. Get to know Hough transform  
2. Develop a detection program for straight lines. 

### 1.1 Hough transform 
Each pixel in the image has infinite crossing lines: y = mx + b ([0,b], [-b/m,0]).
Consider 1 pixel [x0,y0] in x-y domain: b = -x0m + y0 ([0,y0], [y0/x0]) 
Only the straight line has the same [b,m] and this point is the peak in b-m domain. 

![Hough transform](https://user-images.githubusercontent.com/57630290/190166077-f1255603-1b25-42b6-8d2f-8460dbfc4c0e.png)

## 2. Requirments 
1. **cv2** - 
2. **scikit-learn** - import Hough transform functions   
3. **numpy**
4. **matplotlib**

```
import numpy as np
import cv2
from skimage.transform import (hough_line, hough_line_peaks)
from matplotlib import pyplot as plt
```

## 3. Data 
1. loading the image 
2. get the invert image
3. plot both 
```
    figure = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img_orignal, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.imshow(img_invert, cmap='gray')

```
![original_inverted](https://user-images.githubusercontent.com/57630290/190173921-47b4ae3f-dafc-4e54-b40f-d995b72d3806.png)

