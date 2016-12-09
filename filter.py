import matplotlib
matplotlib.use('Agg')

from skimage import data, io, filters, segmentation, color
import matplotlib.pyplot as plt
from Tkinter import *
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

#init Tkinter

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        w = Label(frame, text="Hello, world!")
        w.pack()


root = Tk()
app = App(root)
root.mainloop()
root.destroy()

plt.figure()

io.imshow(filt_real)
io.show()
