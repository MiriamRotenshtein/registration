
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('images/light_blue.png')

rgbArr = np.array(img)

pixels = rgbArr.reshape(-1, 3)

blue = pixels[:, 2]

avgBlueColor = np.average(blue, axis=0)

plt.hist(avgBlueColor, bins=200, range=[0, 256])
plt.title("provide the average of blue pixels in the image")
plt.xlabel("average of blue pixels")
plt.ylabel("Number of pixels")
plt.show()
