import numpy as np
import cv2
from skimage.transform import (hough_line, hough_line_peaks)
from matplotlib import pyplot as plt


class NN:
    def __int__(self):
        pass

    def train(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        shape = X.shape[0]
        Ypred = np.zeros(shape, dtype=self.y_train.dtype)
        for i in range(shape):
            distance = np.sum(np.abs(self.X_train - X[i, :]), axis=1)
            min_index = np.argmin(distance)
            Ypred[i] = self.y_train[min_index]


def main():
    img_orignal = cv2.imread('intersecting-lines.jpg', 0)
    img_invert = ~img_orignal

    figure = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img_orignal, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.imshow(img_invert, cmap='gray')

    angles = np.linespace(-np.pi/2, np.pi/2, 180)



if __name__ == '__main__':
    main()
