from src.data_io.dataset_folder import generate_FT
import cv2
import numpy as np


img = cv2.imread('./images/sample/test_face.jpeg')
img_gay = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print (f'gay : {np.shape(img_gay)},{img_gay[0:50]}')

img_fft = generate_FT(img)
print (f'img_fft : {np.shape(img_fft)},{img_fft[0:50]}')
