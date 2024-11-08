import time 
import os
import pygame

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

def timer(secondesTotale,seconde,minutes):
    for i in range(secondesTotale):
        time.sleep(1)
        seconde = seconde - 1
        if (seconde == 0):
            seconde = 60
            minutes = minutes - 1
        os.system('clear')
        print(f"temps d'etudes : {minutes}:{seconde}")

def main():
    # déclarations du temps
    etude = int(input("vous voulez étudier pour combien de minutes?\n"))
    pause = int(input("combien de temps pour les pause?\n"))

    # convertir minutes en seconde
    seconde_totale_etude = etude * 60
    seconde_totale_pause = pause * 60

    # boucle de l'apps
    while(True):

        # variables affiché par l'apps
        minuteEtude = etude - 1 
        seconde = 60
        minutePause = pause - 1

        # boucle d'étude
        timer(seconde_totale_etude,seconde,minuteEtude) 
        
        # message de pause  
        os.system('clear')
        alarme()
        os.system('clear')
        print(f"pause de {pause} minutes")
        time.sleep(2)

        # boucle de pause
        timer(seconde_totale_pause,seconde,minutePause)
        
        # alarme 
        os.system('clear')
        alarme()
        os.system('clear')
        
        # demande de sortie
        sortie = input("Voulez-vous faire un autre pomodoro?(y/n)\n")
        if (sortie == 'n' or sortie == 'N'):
            break
main()
