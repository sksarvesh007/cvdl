import cv2 
import matplotlib.pyplot as plt 
image = cv2.imread('image.jpeg')
new_img = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
plt.imshow(image)
plt.show()
plt.imshow(new_img, cmap='gray')
plt.show()