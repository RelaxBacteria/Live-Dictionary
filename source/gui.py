import tkinter as Tk
import tkinter.ttk as ttk
import pyscreenshot as ImageGrab
import preProcess
import ocr
import pytesseract
import time
import os.path
from PIL import Image

# Image paths
image_path = '../screenshot.png'
prev_image_path = '../prev.png'

lang_choices = ['eng', 'jpn', 'jpn_vert']
bool_choices = ['yes', 'no']
amount_choices = ['1', '2', '3']

class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Live Dictionary")
        self.root.resizable(0, 0)
        self.root.geometry("420x828+611+11")
        self.frame = Tk.Frame(parent, width=300, height=300)
        self.frame.pack()

        # GUI Design
        self.Operations_LabelFrame = Tk.LabelFrame(self.root)
        self.Operations_LabelFrame.place(relx=0.095, rely=0.013, relheight=0.175, relwidth=0.224)
        self.Operations_LabelFrame.configure(text='''Operations''')
                 
        captureBtn = Tk.Button(self.Operations_LabelFrame, text="Capture", command=self.capture)
        captureBtn.place(relx=0.106, rely=0.214, height=24, width=77, bordermode='ignore')

        ocrBtn = Tk.Button(self.Operations_LabelFrame, text="GO!", command=self.ocr)
        ocrBtn.place(relx=0.106, rely=0.428, height=24, width=77, bordermode='ignore')
        
        self.curr_language = Tk.StringVar(self.frame)
        self.curr_language.set(lang_choices[0])
        
        language_select = Tk.OptionMenu(self.Operations_LabelFrame, self.curr_language, *lang_choices)
        language_select.place(relx=0.106, rely=0.717, height=24, width=77, bordermode='ignore')

        self.text = Tk.Text(self.root)
        self.text.place(relx=0.095, rely=0.55, relheight=0.423, relwidth=0.798)

        # scroll_bar = Tk.Scrollbar(command = self.text.yview)
        # scroll_bar.pack()
        # self.text['yscrollcommand'] = scroll_bar.set

        self.prevImage = Tk.PhotoImage(file=prev_image_path)
        self.image = Tk.Label(self.root, image=self.prevImage)
        self.image.place(relx=0.095, rely=0.225, height=240, width=340)
        self.image.image = self.prevImage

        self.ImageLabelFrame = Tk.LabelFrame(self.root)
        self.ImageLabelFrame.place(relx=0.357, rely=0.013, relheight=0.17, relwidth=0.548)
        self.ImageLabelFrame.configure(text='''Image Manipulation''')

    # Method to check the option is working
    # def changeOption(self, *args):
    #     print(lang_choices[self.curr_language.get()])

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
            # preProcess.preProcess(image_path)
            
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
        self.image.configure(image=self.prevImage)
        self.image.image = self.prevImage

    def ocr(self):
        # Remove all text in the textbox
        self.text.delete(0.0, Tk.END)

        # Display results in the textbox
        self.text.insert(Tk.CURRENT, pytesseract.image_to_string(Image.open(image_path), lang=self.curr_language.get()))
        
        
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