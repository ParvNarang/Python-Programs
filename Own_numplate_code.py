import cv2
import numpy as np
import pytesseract
from PIL import Image

# 1. Load the image
img = cv2.imread("/Users/parvnarang/Desktop/images/n.png")
#img = cv2.imread('1.png')
#config = ('-l eng --oem 1 --psm 3')

# 2. Resize the image
x = Image.open("/Users/parvnarang/Desktop/images/n.png")
#x = Image.open('1.png')
width, height = x.size
print(width,height)

def i():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 4. Convert image to black and white (using adaptive threshold)
    adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

    config = "--psm 3"
    text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
    #print(text)


    alphanumeric = ""
    for character in text:
        if character.isalnum():
            alphanumeric += character
    print(alphanumeric)




    if text[0] != 'D':
        b = text.replace(text[0],'')
        #print(b)
        if b[0] != 'D':
            c = b.replace(b[0],'')
            alphanumeric = ""
            for character in c:
                if character.isalnum():
                    alphanumeric += character
            print(alphanumeric)

    if text[0] != 'D' and text[0] == '"':
        b = text.replace(text[0],'')
        #print(b)
        if b[0] != 'D':
            c = b.replace(b[0],'')
            if c[1] != 'L':
                d = c.replace(c[1],'')
                alphanumeric = ""
                for character in d:
                    if character.isalnum():
                        alphanumeric += character
                print(alphanumeric)

    '''if text[0] != 'D':
        b = text.replace(text[0],'')
        #print(b)
        if b[0] != 'D':
            c = b.replace(b[0],'')
            if c[1] != 'L':
                d = c.replace(c[1],'')
                alphanumeric = ""
                for character in d:
                    if character.isalnum():
                        alphanumeric += character

                print(alphanumeric)'''

    if len(alphanumeric) > 9:
        if alphanumeric[10].isascii() or alphanumeric[10].isascii():
            z = alphanumeric.replace(alphanumeric[10], '')
            if z[10].isascii() or z[10].isascii():
                v = z.replace(z[10], '')
                print(v)


    cv2.imshow("gray", gray)
    cv2.imshow("adaptive th", adaptive_threshold)
    cv2.waitKey(0)

if width < 350 and height < 210:
    img = cv2.resize(img, None, fx=2, fy=1)
    i()

else:
    i()



'''import re 
  
# Function checks if the string 
# contains any special character 
def run(string): 
  
    # Make own character set and pass  
    # this as argument in compile method 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
    if(regex.search(string) == None): 
        print("String is accepted") 
          
    else: 
        print("String is not accepted.")'''
