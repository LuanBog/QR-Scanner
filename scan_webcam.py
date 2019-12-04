import cv2
import sys
import pyzbar.pyzbar as pyzbar
import pyperclip

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

run = True

def clipboard(text):
    pyperclip.copy(text)
    pyperclip.paste()

def process(data):
    data = str(data)

    try:
        first_part = data.split("b\'")
        second_part = first_part[1].split("\'")
    except:
        first_part = data.split("b\"")
        second_part = first_part[1].split("\"")

    return str(second_part[0])

while run:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)

    decodedObjects = pyzbar.decode(frame)

    for obj in decodedObjects:
        #QR CODE GOES HERE
        data = process(obj.data)

        cap.release()
        cv2.destroyAllWindows()

        print("\nQR: {}".format(data))

        cc = input("\nAdd to clipboard?\n(y/n): ")

        if cc.lower() == "yes" or cc.lower() == "y":
            clipboard(data)

        run = False

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
