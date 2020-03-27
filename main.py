import pytesseract
from PIL import Image, ImageEnhance, ImageOps
import numpy
import cv2
pytesseract.pytesseract.tesseract_cmd = r'D:\_Code\_Tesseract\tesseract'

# Grayscale attempt
def test(lang, file):
    print("--------------GRAYSCALE--------------")
    img = Image.open(file).convert('L')
    img_numpy = numpy.array(img, 'uint8')
    cv2.imwrite('testbw.jpg', img_numpy)
    print(pytesseract.image_to_string('testbw.jpg', lang=lang))
    

    # Grayscale + saturation
    print("-------GRAYSCALE+SATURATION(3)-------")
    imgbw = Image.open('testbw.jpg')
    contrastbw = ImageEnhance.Contrast(imgbw)
    imgcontrast = contrastbw.enhance(3)
    imgcontrast.save('testbwcont3.jpg')
    print(pytesseract.image_to_string('testbwcont3.jpg', lang=lang))
    

    print("-------GRAYSCALE+SATURATION(5)-------")
    imgbw = Image.open('testbw.jpg')
    contrastbw = ImageEnhance.Contrast(imgbw)
    imgcontrast = contrastbw.enhance(5)
    imgcontrast.save('testbwcont5.jpg')
    print(pytesseract.image_to_string('testbwcont5.jpg', lang=lang))


    # Inverted Grayscale
    print("-------INVERTED GRAYSCALE------------")
    imgbw = Image.open('testbw.jpg')
    imginvert = ImageOps.invert(imgbw)
    imginvert.save('testbwinvert.jpg')
    print(pytesseract.image_to_string('testbwinvert.jpg', lang=lang))
    

    # Inverted grayscale with saturation
    print("--INVERTED GRAYSCALE+SATURATION(3)---")
    imgbw = Image.open('testbwcont3.jpg')
    imginvert = ImageOps.invert(imgbw)
    imginvert.save('testbwcontinvert3.jpg')
    print(pytesseract.image_to_string('testbwcontinvert3.jpg', lang=lang))
    

    print("--INVERTED GRAYSCALE+SATURATION(5)---")
    imgbw = Image.open('testbwcont5.jpg')
    imginvert = ImageOps.invert(imgbw)
    imginvert.save('testbwcontinvert5.jpg')
    print(pytesseract.image_to_string('testbwcontinvert5.jpg', lang=lang))
    
    
test('rus', 'test.jpeg')

# img = Image.open('test.jpg').convert('L')
# img = Image.open('testbw.jpg')
# contrast = ImageEnhance.Contrast(img)
# imgcontrast = contrast.enhance(1)
# imgcontrast.save('testcont.jpg')
# imginvert = ImageOps.invert(imgcontrast)
# imginvert.save('invert.jpg')
# img_numpy = numpy.array(imgcontrast, 'uint8')
# cv2.imwrite('testbwcont.jpg', img_numpy)

# print("----------jpn--------------------")
# print(pytesseract.image_to_string('invert.jpg', lang='jpn'))
# print("----------jpn_vert--------------------")
# print(pytesseract.image_to_string('invert.jpg', lang='jpn_vert'))
