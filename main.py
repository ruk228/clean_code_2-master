
BUFFER = 1024
FRAMERATE = 60
MORSE_SOUND = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    '|': 'long_silence.ogg',
}
import pygame
pygame.init ()
import os
os.system ('cls||clear')
pygame.mixer.init (BUFFER)
azbukaMorze = {'а': '.-',
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
               '_': '..--.-'}
soobchenie=os.getenv('komanda', default = 'По-умолчанию')
soobchenie=soobchenie.lower()
x=soobchenie[0]
xx=soobchenie[1]
xxx=soobchenie[2]
probel1=soobchenie[3]
y=soobchenie[4]
yy=soobchenie[5]
yyy=soobchenie[6]
probel2=soobchenie[7]
z=soobchenie[8]
zz=soobchenie[9]
zzz=soobchenie[10]
morz=azbukaMorze[x]+azbukaMorze[xx]+azbukaMorze[xxx]+azbukaMorze[probel1]+azbukaMorze[y]+azbukaMorze[yy]+azbukaMorze[yyy]+azbukaMorze[probel2]+azbukaMorze[z]+azbukaMorze[zz]+azbukaMorze[zzz]        
adres='http://195.161.68.58'
import requests
from alive_progress import alive_bar
import time
def svyazatsya_s_robotom( adres ):
    otvet=requests.get( adres )
    soobshchenie = 'Проверка связи с роботом...' 
    print(soobshchenie)
    with alive_bar( len( soobshchenie ),bar = 'brackets',spinner = 'radioactive' ) as bar:
         for _ in range( len( soobshchenie ) ):
              time.sleep(0.06)
              bar( )
    os.system ('cls||clear')          
    if otvet.status_code==200:
        print( 'Связь с роботом установлена!' ) 
    else:
        print( 'Нет связи с роботом' )    
    print( )
svyazatsya_s_robotom(adres)
def igrat_muzyku( soundfile ):
    sound=pygame.mixer.Sound( soundfile )
    clock=pygame.time.Clock( )
    sound.play( )
    while pygame.mixer.get_busy( ):
        clock.tick( FRAMERATE )
def proigrat_muzyku_Morze( morz ):
    print( )
    with alive_bar( len(morz),bar = 'brackets',spinner = 'dots_waves2' ) as bar:
        if   morz[ 0 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 0 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 0 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 1 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 1 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 1 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 2 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 2 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 2 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 3 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 3 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 3 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 4]  == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 4 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 4 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 5 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 5 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 5 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )  
        if   morz[ 6 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 6 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 6 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 7 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 7 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 7 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 8 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 8 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 8 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 9 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 9 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 9 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )   
        if   morz[ 10 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 10 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 10 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 11 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 11 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 11 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 12 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 12 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 12 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 13 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 13 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 13 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 14 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 14 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 14 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 15 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 15 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 15 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 16 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 16 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 16 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 17 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 17 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 17 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 18 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 18 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 18 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 19 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 19 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 19 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 20 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 20 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 20 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 21 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 21 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 21 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 22 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 22 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 22 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
        if   morz[ 23 ] == '.':
             igrat_muzyku(pygame.mixer.Sound( 'dot.ogg' ))
        elif morz[ 23 ] == '-':
             igrat_muzyku(pygame.mixer.Sound( 'dash.ogg' ))
        elif morz[ 23 ] == '|':
             igrat_muzyku(pygame.mixer.Sound( 'long_silence.ogg' ))
        bar( )
    print()
def otpravka_soobshcheniya_robotu(adres, soobshchenie):
    print('Отправка сообщения роботу...')
    otvet = requests.post(adres,soobshchenie.encode('utf-8'))
    if otvet.status_code == 200:
        print('Команда принята.');time.sleep(1);print('Бегу к вам!')
    elif otvet.status_code == 501:
        print('Команда принята. Продолжаю выполнять прежнюю инструкцию.')
    else:
        print('Команда не принята. Не понял вас!')      