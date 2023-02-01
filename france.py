import matplotlib.pyplot as plt
import numpy as np


red = [255, 0, 0]
white = [255, 255, 255]
blue = [0,0, 255]

france_flag = np.array([[blue, white, red], [blue, white, red]])

plt.imshow(france_flag)
plt.show()