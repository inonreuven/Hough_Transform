# Hough_Transform
Straight lines detection with Hough Transform using cv2 and scikit-learn.  

## Contents
1. Objective
  1.1 Hough transform 
2. Requirments 
3. Data 
4. Hough transform 


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

## 4. Hough transform 
1. define upper and lower Theta 
2. define number of samples 
3. create angles axis 
4. Hough transform: *Hough space* - create Hough domain, *theta* values and *r* values of each pixel in the x-y domain
```
theta_min = -np.pi/2
theta_max = np.pi/2
n_samples = 180
angles = np.linspace(theta_min, theta_max, n_samples)
hough_space, theta, r = hough_line(img_invert, angles)
plt.subplot(1, 2, 1)
plt.imshow(img_invert, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(hough_space, cmap='gray')
```

![Hough_domain](https://user-images.githubusercontent.com/57630290/190181850-900847fa-2501-42d8-9646-6b53cd5181fb.png)

