import tkinter as Tk
import pyscreenshot as ImageGrab
import preProcess
import ocr
import pytesseract
import time
from PIL import Image

# Image paths
image_path = '../screenshot.png'
prev_image_path = '../prev.png'

class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Live Dictionary")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
                
        captureBtn = Tk.Button(self.frame, text="Capture", command=self.capture)
        captureBtn.pack()

        ocrBtn = Tk.Button(self.frame, text="GO!", command=self.ocr)
        ocrBtn.pack()
        
        self.text = Tk.Text(self.frame, height=12, wrap='word')
        self.text.pack()

        self.image = Tk.Label(self.frame, text="Preview Image")
        self.image.pack()

    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()
        
    #----------------------------------------------------------------------
    def capture(self):
        
        self.hide()

        # grab fullscreen
        im = ImageGrab.grab()

        # save image file
        im.save(image_path)

        # show image in a window
        # im.show()

        try:
            # Preprocess and overwrite
            preProcess.preProcess(image_path)
            
            # Refresh Image
            self.showPreviewImage()

        except Exception as e:
            print(e)
        finally:
            self.show()
    
    def showPreviewImage(self):
        # Make a preview image
        preProcess.createPreview(image_path, prev_image_path)
        
        # Load and show the preview Image
        self.prevImage = Tk.PhotoImage(file=prev_image_path)
        self.image.configure(image=self.prevImage, text="")
        self.image.image = self.prevImage
        self.image.pack()

    def ocr(self):
        # Remove all text in the textbox
        self.text.delete(0.0, Tk.END)

        # Display results in the textbox
        self.text.insert(Tk.CURRENT, pytesseract.image_to_string(Image.open(image_path)))
        
        print(pytesseract.image_to_string(Image.open(image_path)))

    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()
        
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
        
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()