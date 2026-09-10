import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("sample.jpg")
arr = np.array(img)

red = arr[:, :, 0]
green = arr[:, :, 1]
blue = arr[:, :, 2]

print("--- CHANNEL EXTRACTION SUMMARY ---")
print("Original Image Shape :", arr.shape)
print("Red Channel 2D Shape :", red.shape, "| Mean Intensity:", round(red.mean(), 2))
print("Green Channel 2D Shape:", green.shape, "| Mean Intensity:", round(green.mean(), 2))
print("Blue Channel 2D Shape :", blue.shape, "| Mean Intensity:", round(blue.mean(), 2))
print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")

red_img = np.zeros_like(arr)
red_img[:, :, 0] = red

green_img = np.zeros_like(arr)
green_img[:, :, 1] = green

blue_img = np.zeros_like(arr)
blue_img[:, :, 2] = blue

fig, axs = plt.subplots(2, 3, figsize=(12, 8))

axs[0, 0].imshow(red_img)
axs[0, 0].set_title("Red Only")

axs[0, 1].imshow(green_img)
axs[0, 1].set_title("Green Only")

axs[0, 2].imshow(blue_img)
axs[0, 2].set_title("Blue Only")

axs[1, 0].imshow(red, cmap='gray')
axs[1, 0].set_title("Red Channel Grayscale")

axs[1, 1].imshow(green, cmap='gray')
axs[1, 1].set_title("Green Channel Grayscale")

axs[1, 2].imshow(blue, cmap='gray')
axs[1, 2].set_title("Blue Channel Grayscale")

plt.show()