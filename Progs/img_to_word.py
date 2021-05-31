import cv2
import pytesseract
# read image
#im = cv2.imread('/Users/parvnarang/Desktop/images/check.png')
im = cv2.imread('Resources/2.png')

# configurations
config = ('-l eng --oem 1 --psm 3')
# pytessercat
text = pytesseract.image_to_string(im, config=config)
# print text
#text = text.split('\n')
print(text)
