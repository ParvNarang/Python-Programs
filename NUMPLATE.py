import cv2
import pytesseract
from pytesseract import Output

config = ('-l eng --oem 1 --psm 3')

#img = cv2.imread('f.jpg')
img = cv2.imread('/Users/parvnarang/Desktop/images/4.jpeg')                            ## method can be changed ....
resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))                      ## for reading images.....

fi = open("f.txt","r")
k = open("P","r")


t = fi.read()

# pytesseract
text = pytesseract.image_to_string(resized, config=config)

# print text

d = pytesseract.image_to_data(resized, output_type=Output.DICT)
#print(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        resized = cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

#text = text.split('')
print( ' This is the number plate detected : ',text )
r = input(" ENTER THE CITY CODE FROM THE ABOVE STATEMENT. ")
if r == "DL":
    y = input(" ENTER THE LAST 4 DIGITS OF THE NUMBER PLATE ")

elif r == "MH":
    y = input(" ENTER THE LAST 4 DIGITS OF THE NUMBER PLATE ")

elif r == "PB":
    y = input(" ENTER THE LAST 4 DIGITS OF THE NUMBER PLATE ")

elif r == "HR":
    y = input(" ENTER THE LAST 4 DIGITS OF THE NUMBER PLATE ")

elif r == "HP":
    y = input(" ENTER THE LAST 4 DIGITS OF THE NUMBER PLATE ")

else:
    print(" NOTHING ")


w = open(y,"r")
'''path = '/Users/parvnarang/PycharmProjects/fimac/venv'
if w not in path:
    print("Not here")'''
z =  w.read()

if text in t:
    print(" YES IT IS PRESENT ")
    u = input(" DO YOU WANT ITS DETAILS ? ")
    if u == "yes" or u == "YES" or u == "Yes":
        print( z )

    elif u == "NO" or u == "no" or u == "No":
        print(" OK BYE ")
        exit()

    else:
        print(" SORRY COULD NOT GET YOU TRY AGAIN ")
        exit()



else:
    print(" NOTHING TO SHOW .")
cv2.imshow('img', resized)
'''while True:
    key = cv2.waitKey(1)

    if key == ord('q'):
        break'''
cv2.waitKey(0)
