import cv2
import pytesseract
from pytesseract import Output

config = ('-l eng --oem 1 --psm 3')
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # convert to grayscale
    '''gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # create a binary thresholded image
    _, binary = cv2.threshold(gray, 255 // 2, 255, cv2.THRESH_BINARY_INV)
    # find the contours from the thresholded image
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # draw all contours
    image = cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    # show the images
    #cv2.imshow("gray", gray)'''
    text = pytesseract.image_to_string(frame, config=config)
    d = pytesseract.image_to_data(frame, output_type=Output.DICT)

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            resized = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("image", frame)

    print(text)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
