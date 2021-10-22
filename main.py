import pygame
import os
import time
import requests
from dotenv import load_dotenv
from alive_progress import alive_bar

BUFFER = 1024
FRAMERATE = 60
MORSE_SOUND = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    '|': 'long_silence.ogg',
    }


def send_message_robot(adres):
    answer = requests.post(adres)

    if answer.status_code == 200:
        time.sleep(1)
    elif answer.status_code == 501:
        print('Команда не принята. Не понял вас!')    

 
def contact_the_robot(adres):
    answer = requests.get(adres)
    message = 'Проверка связи с роботом...' 

    with alive_bar(len(message), bar='brackets', spinner='radioactive') as bar:

        for _ in range(len(message)):
            time.sleep(0.06)
            bar()

    os.system('cls||clear')    

    if answer.status_code == 200:
        print('Связь с роботом установлена!') 
    else:
        print('Нет связи с роботом')    


def play_music(soundfile):
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()

    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)


def play_morse_music(morz):
    with alive_bar(len(morz), bar='brackets', spinner='dots_waves2') as bar:
        for num in range(len(morz)):
            if morz[num] == '.':
                play_music(pygame.mixer.Sound('dot.ogg'))
            elif morz[num] == '-':
                play_music(pygame.mixer.Sound('dash.ogg'))
            elif morz[num] == '|':
                play_music(pygame.mixer.Sound('long_silence.ogg'))
            bar()


if __name__ == '__main__':
    load_dotenv()
    pygame.init()
    os.system('cls||clear')
    pygame.mixer.init(BUFFER)
    adres = 'http://195.161.68.58'
    azbukaмorze = {
                'а': '.-',
                'б': '-...',
                'в': '.--',
                'г': '--.',
                'д': '-..',
                'е': '.',
                'ж': '...-',
                'з': '--..',
                'и': '..',
                'й': '.---',
                'к': '-.-',
                'л': '.-..',
                'м': '--',
                'н': '-.',
                'о': '---',
                'п': '.--.',
                'р': '.-.',
                'с': '...',
                'т': '-',
                'у': '..-',
                'ф': '..-.',
                'х': '....',
                'ц': '-.-.',
                'ч': '---.',
                'ш': '----',
                'щ': '--.-',
                'ъ': '.--.-.',
                'ы': '-.--',
                'ь': '-..-',
                'э': '..-..',
                'ю': '..--',
                'я': '.-.-',
                '1': '.----',
                '0': '-----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.',
                ',': '--..--',
                '.': '.-.-.-',
                '?': '..--..',
                ';': '-.-.-.',
                ':': '---...',
                "'": '.----.',
                '-': '-....-',
                '/': '-..-.',
                '(': '-.--.-',
                ')': '-.--.-',
                ' ': '|',
                '_': '..--.-'
                }
    message = os.getenv('KOMANDA', default='По-умолчанию').lower()
    morz = ''

    contact_the_robot(adres)
    send_message_robot(adres)

    for symbol in message:
        morz += azbukaмorze[symbol]
    play_morse_music(morz)
