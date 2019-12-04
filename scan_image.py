import cv2
import pyzbar.pyzbar as pyzbar
import pyperclip

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

if __name__ == "__main__":
    path = input("\nPlease put the path: ")

    image = cv2.imread(path)

    decodedObjects = pyzbar.decode(image)

    for obj in decodedObjects:
        data = process(obj.data)

        print("\nQR: {}".format(data))

        cc = input("\nAdd to clipboard?\n(y/n): ")

        if cc.lower() == "yes" or cc.lower() == "y":
            clipboard(data)
