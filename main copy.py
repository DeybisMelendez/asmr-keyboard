from pynput import mouse
from pynput import keyboard
from playsound import playsound
key_history = []
def on_click(x, y, button, pressed):
    if pressed:
        playsound("assets/sounds/clickdown.wav")
    else:
        playsound("assets/sounds/clickup.wav")

def on_press(key):
    if not key in key_history:
        key_history.clear()
        key_history.append(key)
        playsound("assets/sounds/keydown.ogg")
def on_release(key):
    if key in key_history:
        key_history.remove(key)
        playsound("assets/sounds/keyup.ogg")

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener.start()
mouse_listener.start()

while True:
    pass