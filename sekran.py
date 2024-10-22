from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
from pynput.mouse import Listener, Button, Controller
import pyscreenshot
import pyautogui
import os

print("EKRAN GÖRÜNTÜSÜNÜ KIRPARAK KAYDETMEK İÇİN")
print("Mouse 'un bulunduğu yeri baz alarak Print Screen tuşuna basın")

global x0, y0
def on_click(x1, y1, button, pressed):
    global x0, y0
    if button == Button.left and pressed:
        try:
            if x0 > x1:
                z = x0
                x0 = x1
                x1 = z
            if y0 > y1:
                z = y0
                y0 = y1
                y1 = z
            if x0 == x1:
                x1 = x1+1
            if y0 == y1:
                y1 = y1+1

            im = pyscreenshot.grab(bbox=(x0, y0, x1, y1))
            im.save("ekran-goruntusu.png")
            konum = os.getcwd()
            print("\nEKRAN GÖRÜNTÜSÜ " + konum + " KONUMUNA KAYDEDİLDİ.")
            print("\nTekrar ekran görüntüsü almak için mouse 'un bulunduğu yeri baz alarak Print Screen tuşuna basın")
            return False
        except Exception as exc:
            print(exc)
            pass

    return True

def on_press(k):
    global x0, y0
    if k == Key.print_screen:
        mouse = pyautogui.position()
        x0, y0 = mouse[0], mouse[1]
        print("Mouse 'un bulunduğu yeri baz alarak mouse 'un sol tuşuna tıklayın..")

        with Listener(on_click=on_click) as listener:
            try:
                listener.join()
            except Exception as exc:
                print(exc)
                pass

keyboard_listener = KeyboardListener(on_press=on_press)
keyboard_listener.start()
keyboard_listener.join()