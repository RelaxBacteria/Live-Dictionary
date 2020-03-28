import pytesseract
from PIL import Image, ImageEnhance, ImageOps
import numpy
import cv2
pytesseract.pytesseract.tesseract_cmd = r'D:\_Code\_Tesseract\tesseract'

# Grayscale attempt
def ocrUnit(lang, file):
    result = ""

    # Converting image to grayscale for better recognition and saving the file to use ImageEnhance
    print("--------------GRAYSCALE--------------")
    img = Image.open(file).convert('L')
    img_bw = numpy.array(img, 'uint8')
    cv2.imwrite('testbw.jpg', img_bw)
    result += " " + pytesseract.image_to_string(img_bw, lang=lang).replace("\n", " ")
    print(pytesseract.image_to_string(img_bw, lang=lang))
    
    print("-------GRAYSCALE+CONTRAST(5)-------")
    contrastbw = ImageEnhance.Contrast(Image.open('testbw.jpg'))
    img_bw_cont_5 = contrastbw.enhance(5)
    img_bw_cont_5.save('testbwcont5.jpg')
    result += " " + pytesseract.image_to_string(img_bw_cont_5, lang=lang).replace("\n", " ")
    print(pytesseract.image_to_string(img_bw_cont_5, lang=lang))

    # Inverted Grayscale
    print("-------INVERTED GRAYSCALE------------")
    imgbw = Image.open('testbw.jpg')
    img_bw_invert = ImageOps.invert(Image.open('testbw.jpg'))
    result += " " + pytesseract.image_to_string(img_bw_invert, lang=lang).replace("\n", " ")
    print(pytesseract.image_to_string(img_bw_invert, lang=lang))
    
    print("--INVERTED GRAYSCALE+CONTRAST(5)---")
    img_bw_cont_5_invert = ImageOps.invert(Image.open('testbwcont5.jpg'))
    result += " " + pytesseract.image_to_string(img_bw_cont_5_invert, lang=lang).replace("\n", " ")
    print(pytesseract.image_to_string(img_bw_cont_5_invert, lang=lang))

    words_list = result.split(" ")
    filter_object = filter(lambda x: x != "", words_list)
    words_list_no_empty = list(filter_object)

    # list containing results that more than two conversions agree
    final_list = []
    for word in words_list_no_empty:
        if words_list_no_empty.count(word) >= 2:
            final_list.append(word.strip(" "))
    final_set = set(final_list)
    print(final_set)



    # words_set = set(words_list_no_empty)
    # print(words_set)
    
ocrUnit('rus', 'test_rus.jpeg')

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
