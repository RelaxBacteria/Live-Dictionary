import tkinter as Tk
import tkinter.ttk as ttk
import pyscreenshot as ImageGrab
import preProcess
import ocr
import pytesseract
import time
import os.path
import tkinter.messagebox as TkMsg
from PIL import Image

# Image paths
image_path = '../screenshot.png'
prev_image_path = '../prev.png'
target_image_path = '../target.png'



lang_choices = ['eng', 'jpn', 'jpn_vert', 'rus', 'chi']
bool_choices = ['yes', 'no']
amount_choices = ['None', '1', '2', '3']


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
        self.is_edited = False

        # GUI Design
        self.Operations_LabelFrame = Tk.LabelFrame(self.root)
        self.Operations_LabelFrame.place(relx=0.095, rely=0.013, relheight=0.175, relwidth=0.224)
        self.Operations_LabelFrame.configure(text='''Operations''')

        #------- LABELFRAME ---------------------------------------------------------------------#
        captureBtn = Tk.Button(self.Operations_LabelFrame, text="Capture", command=self.capture)
        captureBtn.place(relx=0.106, rely=0.214, height=24, width=77, bordermode='ignore')

        ocrBtn = Tk.Button(self.Operations_LabelFrame, text="GO!", command=self.ocr)
        ocrBtn.place(relx=0.106, rely=0.428, height=24, width=77, bordermode='ignore')
        
        self.curr_language = Tk.StringVar(self.frame)
        self.curr_language.set(lang_choices[0])
        
        language_select = Tk.OptionMenu(self.Operations_LabelFrame, self.curr_language, *lang_choices)
        language_select.place(relx=0.106, rely=0.717, height=24, width=77, bordermode='ignore')

        #------- ROOT --------------------------------------------------------------------------#
        self.text = Tk.Text(self.root)
        self.text.place(relx=0.095, rely=0.55, relheight=0.423, relwidth=0.798)

        # scroll_bar = Tk.Scrollbar(command = self.text.yview)
        # scroll_bar.pack()
        # self.text['yscrollcommand'] = scroll_bar.set

        self.image = Tk.Label(self.root, text="Preview Image")
        self.image.place(relx=0.095, rely=0.225, height=240, width=340)

        #------ IMAGE MANIPULATION -----------------------------------------------------------#
        self.ImageLabelFrame = Tk.LabelFrame(self.root)
        self.ImageLabelFrame.place(relx=0.357, rely=0.013, relheight=0.17, relwidth=0.548)
        self.ImageLabelFrame.configure(text='''Image Manipulation''')

        self.ApplyButton = Tk.Button(self.ImageLabelFrame, text="Apply", command=self.imageManipulate)
        self.ApplyButton.place(relx=0.696, rely=0.78, height=24, width=57, bordermode='ignore')

        # Grayscale check
        self.grayCheck = Tk.BooleanVar()
        self.grayCheck.set(False)

        self.GrayCheck = Tk.Checkbutton(self.ImageLabelFrame, text="BW", var=self.grayCheck)
        self.GrayCheck.place(relx=0.043, rely=0.142, relheight=0.184, relwidth=0.265, bordermode='ignore')

        # Threashold drop
        # self.Threashold_label = Tk.Label(self.ImageLabelFrame, text="Threashold: ")
        # self.Threashold_label.place(relx=0.348, rely=0.142, relheight=0.184, relwidth=0.265, bordermode='ignore')

        self.Threashold_level = Tk.BooleanVar()
        self.Threashold_level.set(False)

        self.Threashold_select = Tk.Checkbutton(self.ImageLabelFrame, text="Thresholding", var=self.Threashold_level)
        self.Threashold_select.place(relx=0.348, rely=0.142, relheight=0.184, relwidth=0.4, bordermode='ignore')

        

    # Method to check the option is working
    # def changeOption(self, *args):
    #     print(lang_choices[self.curr_language.get()])

    def imageManipulate(self):
        # Give the settings values on the image manipulation frame and make a target.png file, returns True if any edit was done
        self.is_edited = preProcess.preProcess(image_path, target_image_path, self.grayCheck.get(), self.Threashold_level.get())
        
        if self.is_edited:
            self.showPreviewImage(target_image_path)
        else:
            self.showPreviewImage()

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
        self.is_edited = False

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
    
    def showPreviewImage(self, image=image_path):
        # Make a preview image
        preProcess.createPreview(image, prev_image_path)
        
        # Load and show the preview Image
        self.prevImage = Tk.PhotoImage(file=prev_image_path)
        self.image.configure(image=self.prevImage, text="")
        self.image.image = self.prevImage

    def ocr(self):
        # Remove all text in the textbox
        self.text.delete(0.0, Tk.END)

        # Display results in the textbox
        try:
            if self.is_edited:
                self.text.insert(Tk.CURRENT, pytesseract.image_to_string(Image.open(target_image_path), lang=self.curr_language.get()))
            else:
                self.text.insert(Tk.CURRENT, pytesseract.image_to_string(Image.open(image_path), lang=self.curr_language.get()))

        except pytesseract.pytesseract.TesseractError as t:
            self.alert('No train data for the language was detacted.')
        
    def alert(self, message):
        TkMsg.showwarning("Warning!", message)

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