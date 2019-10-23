import random

import keyboard
from playsound import playsound

sound_path = 'sounds/'
typing_sounds = [
    'key01.wav',
    'key02.wav',
    'key03.wav',
    'key04.wav',
    'key05.wav',
    'key06.wav',
    'key07.wav',
    'key08.wav'
]
enter_sound = 'ding01.wav'


def pick_sound(event):
    name = event.name
    if name in ['shift', 'ctrl', 'alt', 'caps lock']:
        # TODO: get a non-clicking sound for these
        return
    elif name == 'enter':
        sound = enter_sound
    else:
        sound = random.choice(typing_sounds)
    return f'{sound_path}/{sound}'


def play_sound(sound):
    playsound(sound, block=False)


def play(event):
    try:
        sound = pick_sound(event)
        if sound:
            play_sound(sound)
    except Exception as ex:
        raise


if __name__ == '__main__':
    keyboard.on_press(play)
    keyboard.wait()
