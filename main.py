import time 
import os
import pygame
from modules import *

# constante d'affichage de statut
ETUDE="study"
PAUSE="break"

def main():

    # ascii art début de jeux
    clear() # clear message de pygames
    # déclarations du temps
    etude = int(input("vous voulez étudier pour combien de minutes?\n"))
    pause = int(input("combien de temps pour les pauses?\n"))
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

        # boucle de pause
        timer(seconde_totale_pause,seconde,minutePause,PAUSE)
        
        # message de sortie
        alarmeAffiché()
        sortie = input("Voulez-vous faire un autre pomodoro?(y/n)\n")
        if (sortie == 'n' or sortie == 'N'):
            break
main()
