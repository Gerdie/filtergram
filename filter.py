import matplotlib
matplotlib.use('Agg')

from skimage import data, io, filters, segmentation, color
import matplotlib.pyplot as plt

#using camera pic as test example
camera = data.camera()

print type(camera)
print "Shape of image: ", camera.shape
print "Number of pixels: ", camera.size
print "Max val: ", camera.max()
print "Min val: ", camera.min()
print "Mean val: ", camera.mean()

#detecting edges with gabor filter
filt_real, filt_imag = filters.gabor(camera, frequency=0.6)

plt.figure()

io.imshow(filt_real)
io.show()
