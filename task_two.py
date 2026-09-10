import numpy as np
from PIL import Image

img = np.zeros((300, 400, 3), dtype=np.uint8)

h, w, c = img.shape
half_h = h // 2
half_w = w // 2

img[0:half_h, 0:half_w] = [255, 0, 0]
img[0:half_h, half_w:w] = [0, 255, 0]
img[half_h:h, 0:half_w] = [0, 0, 255]
img[half_h:h, half_w:w] = [255, 255, 255]

print("Shape:", img.shape)
print("Dtype:", img.dtype)
print("Size:", img.size)
print("Nbytes:", img.nbytes)

Image.fromarray(img).show()
