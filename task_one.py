import math

Wpx = int(input("Enter horizontal pixels (Wpx): "))
Hpx = int(input("Enter vertical pixels (Hpx): "))
Dinches = float(input("Enter screen diagonal in inches (Dinches): "))

total_pixels = Wpx * Hpx

g = math.gcd(Wpx, Hpx)
ratio_w = Wpx // g
ratio_h = Hpx // g

diagonal_px = math.sqrt(Wpx**2 + Hpx**2)
dpi = diagonal_px / Dinches
dpi = round(dpi, 2)

print("Total Pixels:", total_pixels)
print("Aspect Ratio:", str(ratio_w) + ":" + str(ratio_h))
print("DPI:", dpi)

if dpi < 100:
    print("Low Density (Standard Monitor)")
elif dpi <= 200:
    print("Medium Density (HD Display)")
else:
    print("High Density (Retina / Mobile)")