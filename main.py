from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key
import simpleaudio as sa
import random
clickdown = sa.WaveObject.from_wave_file("assets/sounds/clickdown.wav")
clickup = sa.WaveObject.from_wave_file("assets/sounds/clickup.wav")
key_sounds = [
    [
        sa.WaveObject.from_wave_file("assets/sounds/keydown.wav"),
        sa.WaveObject.from_wave_file("assets/sounds/keyup.wav")
    ],
    [
        sa.WaveObject.from_wave_file("assets/sounds/keydown2.wav"),
        sa.WaveObject.from_wave_file("assets/sounds/keyup2.wav")
    ],
    [
        sa.WaveObject.from_wave_file("assets/sounds/keydown3.wav"),
        sa.WaveObject.from_wave_file("assets/sounds/keyup3.wav")
    ]
]

spacedown = sa.WaveObject.from_wave_file("assets/sounds/spacedown.wav")
spaceup = sa.WaveObject.from_wave_file("assets/sounds/spaceup.wav")
key_history = []
def on_click(x, y, button, pressed):
    if pressed:
        clickdown.play()
    else:
        clickup.play()

def on_press(key):
    if not key in key_history:
        key_history.append(key)
        if key == Key.space or key == Key.enter:
            spacedown.play()
        else:
            key_sounds[random.randint(0,2)][0].play()
def on_release(key):
    if key in key_history:
        key_history.remove(key)
        if key == Key.space or key == Key.enter:
            spaceup.play()
        else:
            key_sounds[random.randint(0,2)][1].play()

keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener.start()
mouse_listener.start()

while True:
    pass