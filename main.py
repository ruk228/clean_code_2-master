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


def send_message_robot(adres, soobshchenie):
    print('Отправка сообщения роботу...')
    answer = requests.post(adres, soobshchenie.encode('utf-8'))

    if answer.status_code == 200:
        print('Команда принята.')
        time.sleep(1)
        print('Бегу к вам!')
    elif answer.status_code == 501:
        print('Команда принята. Продолжаю выполнять прежнюю инструкцию.')
    else:
        print('Команда не принята. Не понял вас!')    


def contact_the_robot(adres):
    answer = requests.get(adres)
    soobshchenie = 'Проверка связи с роботом...' 
    print(soobshchenie)

    with alive_bar(len(soobshchenie), bar='brackets', spinner='radioactive') as bar:

        for _ in range(len(soobshchenie)):
            time.sleep(0.06)
            bar()

    os.system('cls||clear')    

    if answer.status_code == 200:
        print('Связь с роботом установлена!') 
    else:
        print('Нет связи с роботом')    

    print()


def igrat_muzyku(soundfile):
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()

    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)


def proigrat_muzyku_Morze(morz):
    with alive_bar(len(morz), bar='brackets', spinner='dots_waves2') as bar:
        for num in range(24):
            if morz[num] == '.':
                igrat_muzyku(pygame.mixer.Sound('dot.ogg'))
            elif morz[num] == '-':
                igrat_muzyku(pygame.mixer.Sound('dash.ogg'))
            elif morz[num] == '|':
                igrat_muzyku(pygame.mixer.Sound('long_silence.ogg'))
            bar()
    print()


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
    send_message_robot(adres, 'ыыы')

    for symbol in message:
        morz += azbukaмorze[symbol]
#изменить названия
#сокр все что возможно
