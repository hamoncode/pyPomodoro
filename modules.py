
import time 
import os
import pygame

def print_ascii_Art():
    print("""
    ____  _  _  __  __  _____  ____  _____  ____  _____ 
    (  _ \\( \\/ )(  \\/  )(  _  )(  _ \\(  _  )(  _ \\(  _  )
    )___/ \\  /  )    (  )(_)(  )(_) ))(_)(  )   / )(_)( 
    (__)   (__) (_/\\/\\_)(_____)(____/(_____)(_)\\_)(_____)
        
        """)

# fonction qui joue l'alarme
def alarme():
    pygame.mixer.init()
    pygame.mixer.music.load('./alarmSound/mixkit-retro-game-emergency-alarm-1000.wav')
    pygame.mixer.music.play(-1) # -1 joue la chanson en boucle
    stop = input("enter pour arreter l'alarme\n")
    if (stop != "df34f2f3f3gsag454/bvrf"):
       pygame.mixer.music.stop()

def alarmeAffiché():
    os.system('clear')
    alarme()
    os.system('clear')

# fonction d'un timer
def timer(secondesTotale,seconde,minutes):
    for i in range(secondesTotale):
        time.sleep(1)
        seconde = seconde - 1
        if (seconde == 0):
            seconde = 60
            minutes = minutes - 1
        os.system('clear')
        print(f"temps d'etudes : {minutes}:{seconde}")

