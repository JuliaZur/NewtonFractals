# Newton fractals
from PIL import Image
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))

xa = -1.0
xb = 1.0
ya = -1.0
yb = 1.0

maxIt = 30
h = 1e-6 
eps = 1e-3 #error allowed

# function for generating fractal
def f(z):
    return z*z*z*z*z*z + z*z*z - 1

for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1) + ya
    for x in range(imgx):
        zx = x * (xb - xa) / (imgx - 1) + xa
        z = complex(zx, zy)
        for i in range(maxIt):
            dz = (f(z + complex(h, h)) - f(z)) / complex(h, h)
            z0 = z - f(z) / dz #Newton iteration
            if abs(z0 - z) < eps: #enough accurate
                break
            z = z0
        image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

image.save("newton4.png", "PNG")
