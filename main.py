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
    pygame.mixer.music.play(-1)
    stop = input("enter pour arreter l'alarme\n")
    if (stop != "df34f2f3f3gsag454/bvrf"):
       pygame.mixer.music.stop() 

# déclarations du temps
etude = int(input("vous voulez étudier pour combien de minutes?\n"))
pause = int(input("combien de temps pour les pause?\n"))


# convertir minutes en seconde
minutes_en_seconde_etude = etude * 60
minutes_en_seconde_pause = pause * 60

# condition de sortie de boucle
autrePomodoro = True

# boucle de l'apps
while(autrePomodoro):

    # variables affiché par l'apps
    minuteEtude = etude - 1 
    seconde = 59
    minutePause = pause - 1

    # boucle d'étude
    for i in range(minutes_en_seconde_etude):
        time.sleep(1)
        seconde = seconde - 1
        if (seconde == 0):
            seconde = 59
            minuteEtude = minuteEtude - 1
        os.system('clear')
        print(f"temps d'etudes : {minuteEtude}:{seconde}")
    
    # message de pause  
    os.system('clear')
    alarme()
    print(f"pause de {pause} minutes")
    time.sleep(2)

    # boucle de pause
    for i in range(minutes_en_seconde_pause):
        time.sleep(1)
        seconde = seconde - 1
        if (seconde == 0):
            seconde = 59
            minutePause = minutePause - 1
        os.system('clear')
        print(f"{minutePause}:{seconde} de pause")
    os.system('clear')
    alarme()
    os.system('clear')
    # demande de sortie
    sortie = input("Voulez-vous faire un autre pomodoro?(y/n)\n")
    if (sortie == 'n' or sortie == 'N'):
        autrePomodoro = False
