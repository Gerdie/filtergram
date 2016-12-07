from skimage import data, io, filters, segmentation, color
import matplotlib.pyplot as plt

#using coffee pic as test example
coffee = skimage.data.coffee()

#detecting edges with gabor filter
filt_real, filt_imag = skimage.filters.gabor(coffee, frequency=0.6)

plt.figure()

io.imshow(filt_real)
io.show()
