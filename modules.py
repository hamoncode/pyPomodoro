
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

"""
clear screen
choisi ainsi au lieu de os a cause plus consistent avec les dockers containers
"""
def clear():
    print("\033[2J\033[H", end="")
    
# fonction qui joue l'alarme
def alarme():
    pygame.mixer.init()
    pygame.mixer.music.load('./alarmSound/mixkit-retro-game-emergency-alarm-1000.wav')
    pygame.mixer.music.play(-1) # -1 joue la chanson en boucle
    stop = input("enter pour arreter l'alarme\n")
    if (stop != "df34f2f3f3gsag454/bvrf"):
       pygame.mixer.music.stop()

# affiche l'alarme 
def alarmeAffiché():
    clear()
    print('temps écoulé')
    alarme()
    clear()

# fonction d'un timer
def timer(secondesTotale,seconde,minutes):
    for i in range(secondesTotale):
        time.sleep(1)
        seconde = seconde - 1
        if (seconde == 0):
            seconde = 60
            minutes = minutes - 1
        clear()
        print(f"temps d'etudes : {minutes}:{seconde}")

