
import time 
import os
import pygame
from tqdm import tqdm

def print_ascii_Art():
    print("""
 _______           _______  _______  ______   _______  _______  _______ 
(  ____ )|\\     /|(       )(  ___  )(  __  \\ (  ___  )(  ____ )(  ___  )
| (    )|( \\   / )| () () || (   ) || (  \\  )| (   ) || (    )|| (   ) |
| (____)| \\ (_) / | || || || |   | || |   ) || |   | || (____)|| |   | |
|  _____)  \\   /  | |(_)| || |   | || |   | || |   | ||     __)| |   | |
| (         ) (   | |   | || |   | || |   ) || |   | || (\\ (   | |   | |
| )         | |   | )   ( || (___) || (__/  )| (___) || ) \\ \\__| (___) |
|/          \\_/   |/     \\|(_______)(______/ (_______)|/   \\__/(_______)
                                                                        
        """)

"""
clear screen
choisi ainsi au lieu de os a cause plus consistent avec les dockers containers
"""

def clear():
    print("\033[2J\033[H", end="")
    print_ascii_Art()
    
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

# fonction d'un timer avec progress bar
def timer(secondesTotale,seconde,minutes,status):
    pbar = tqdm(total=secondesTotale, bar_format='{l_bar}{bar}|')
    pbar.write(f"     {status} time: {minutes}:{seconde}")
    for i in range(secondesTotale):
        time.sleep(1)
        seconde = seconde - 1
        if (seconde == 0):
            seconde = 60
            minutes = minutes - 1
        clear()
        # print avec pbar: fix race condition
        pbar.write(f"     {status} time: {minutes}:{seconde}")
        pbar.update(1)
    pbar.close()

