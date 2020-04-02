from tkinter import *
import pyscreenshot as ImageGrab

master = Tk()

def callback():
    # grab fullscreen
    im = ImageGrab.grab()

    # save image file
    im.save('screenshot.png')

    # show image in a window
    im.show()

b = Button(master, text="OK", command=callback)
b.pack()

mainloop()