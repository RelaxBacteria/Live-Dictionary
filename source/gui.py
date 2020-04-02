from tkinter import *
import pyscreenshot as ImageGrab
import preProcess
import cv2

master = Tk()

def callback():
    # grab fullscreen
    im = ImageGrab.grab()

    # save image file
    filename = "Screenshot.png"
    im.save(filename)

    # show image in a window
    # im.show()

    # Send the image to preProcess.py for preprocessing and overwrite
    preProcess.preProcess(filename)


b = Button(master, text="OK", command=callback)
b.pack()

mainloop()