# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import random as r
plot(range(100), [r.randint(0,10) for i in range(100) ])

# <codecell>

from PIL import Image
import pylab
dino = Image.open("412.jpg")
pylab.imshow(dino)

# <codecell>

land = Image.open("826.jpg")
pylab.imshow(land)
pylab.show()
hist = land.histogram()
pylab.hist(hist,bins=40)

# <codecell>

from PIL import ImageFilter
im1 = dino.filter(ImageFilter.BLUR)
pylab.imshow(im1)

# <codecell>

im2 = dino.filter(ImageFilter.FIND_EDGES)
pylab.imshow(im2)

# <codecell>

im3 = land.filter(ImageFilter.EDGE_ENHANCE_MORE)
pylab.imshow(im3)

# <codecell>

im4 = land.filter(ImageFilter.CONTOUR)
pylab.imshow(im4)

# <codecell>

from PIL import ImageOps
im5 = ImageOps.invert(dino)
pylab.imshow(im5)

# <codecell>

im6 = ImageOps.grayscale(dino)
pylab.imshow(im6)

# <codecell>

im7 = ImageOps.solarize(dino, threshold=128)
pylab.imshow(im7)

# <codecell>

im8 = land.transpose(Image.ROTATE_270)
pylab.imshow(im8)

# <codecell>

im8 = land.transpose(Image.FLIP_TOP_BOTTOM)
pylab.imshow(im8)

# <codecell>

im9 = land.crop((20, 20, 200, 100))
pylab.imshow(im9)

# <codecell>


