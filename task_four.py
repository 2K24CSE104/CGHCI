import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("sample.jpg")
arr = np.array(img)

N = 8

downsampled = arr[::N, ::N, :]

re_expanded = np.repeat(downsampled, N, axis=0)
re_expanded = np.repeat(re_expanded, N, axis=1)

orig_shape = arr.shape
down_shape = downsampled.shape
re_shape = re_expanded.shape

orig_mem = arr.nbytes
down_mem = downsampled.nbytes

dim_reduction = (1 - (1 / N)) * 100
mem_savings = (1 - (down_mem / orig_mem)) * 100

print("--- DOWNSAMPLING ANALYSIS (N =", N, ") ---")
print("Original Shape :", orig_shape, "| Memory:", orig_mem, "bytes")
print("Downsampled Shape :", down_shape, "| Memory:", down_mem, "bytes")
print("Re-expanded Shape :", re_shape, "| Visual: Blocky Pixelation")
print("Dimension Reduction: ", round(dim_reduction, 2), "% reduction per axis")
print("Memory Savings : ", round(mem_savings, 2), "% data reduction")

fig, axs = plt.subplots(1, 2, figsize=(10, 6))

axs[0].imshow(arr)
axs[0].set_title("Original")

axs[1].imshow(re_expanded)
axs[1].set_title("Pixelated (N=8)")

plt.show()