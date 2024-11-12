import time 
import os
import pygame
from modules import *

# constante d'affichage de statut
ETUDE="'etude"
PAUSE="e pause"

def main():

    # ascii art début de jeux
    clear() # clear message de pygames
    
    # déclaration des variables avec vérification char -> int
    etude = is_valid_number(ETUDE)
    pause = is_valid_number(PAUSE)

    clear() # clear l'affichage initiale de la barre
    # convertir minutes en seconde
    seconde_totale_etude = etude * 60
    seconde_totale_pause = pause * 60

    # boucle de l'apps
    while(True):

        # réinitialiser variables affichés par l'apps
        minuteEtude = etude - 1 
        seconde = 60
        minutePause = pause - 1

        # boucle d'étude
        timer(seconde_totale_etude,seconde,minuteEtude,ETUDE)  
        # message de pause  
        alarmeAffiché()
        print(f"pause de {pause} minutes")
        time.sleep(2)
        clear()

        # boucle de pause
        timer(seconde_totale_pause,seconde,minutePause,PAUSE)
        
        # message de sortie
        clear()
        sortie = input("Voulez-vous faire un autre pomodoro?(y/n)\n")
        if ('n' in sortie or 'N' in sortie):
            message_de_fin()
            break
        clear()
main()
