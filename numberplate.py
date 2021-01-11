import cv2
import pytesseract
from pytesseract import Output

config = ('-l eng --oem 1 --psm 3')


e = int(input(" Which number plate you want to see ? "))

if e == 1:
    print("You entered 1 and the number plate is -")
    img = cv2.imread('/Users/parvnarang/Desktop/images/1.jpeg')
    resized = cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))

if e == 2:
    print("You entered 2 and the number plate is -")
    img = cv2.imread('/Users/parvnarang/Desktop/images/2.jpg')
    resized = cv2.resize(img,(int(img.shape[1]/1),int(img.shape[0]/1)))

if e == 3:
    print("You entered 3 and the number plate is -")
    img = cv2.imread('/Users/parvnarang/Desktop/images/3.jpeg')
    resized = cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))


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
print( text )

cv2.imshow('img', resized)
while True:
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
cv2.waitKey(0)