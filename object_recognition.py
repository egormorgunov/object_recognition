from skimage import io, filters
from matplotlib import pyplot as plt

"""Loading Images"""
img1 = io.imread("Training/Pear/1_100.jpg")
img2 = io.imread("Training/Tangerine/1_100.jpg")

"""Converting image to halftone format"""
img1gray = io.imread("Training/Pear/1_100.jpg", as_gray=True)
img2gray = io.imread("Training/Tangerine/1_100.jpg", as_gray=True)

"""Applying Scharr filter"""
img1Scharr = filters.scharr(img1gray)
img2Scharr = filters.scharr(img2gray)

"""Displaying results"""
io.imshow(img1Scharr)
plt.figure()
io.imshow(img2Scharr)
io.show()

"""Defining an Image"""
i = 0

"""Vertical and Horizontal sum for the first Image"""
sum1 = 0
sum2 = 0
"""Vertical and Horizontal sum for the second Image"""
sum3 = 0
sum4 = 0
for i in range(20):
    sum1 += img1Scharr[50][i]
    sum2 += img1Scharr[i][50]
    sum3 += img2Scharr[50][i]
    sum4 += img2Scharr[i][50]
if sum1 < 1 and sum2 > 1:
    print('First image is tangerine')
else:
    print('First picture is pear')
if sum3 < 1 and sum4 > 1:
    print('Second image is tangerine')
else:
    print('Second picture is pear')
