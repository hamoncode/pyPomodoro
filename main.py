import time 
import os

print("""\
             eeeeee                                              
eeeee e    e 8    8 eeeee eeeeeee eeeee eeeee eeeee eeeee  eeeee 
8   8 8    8 8eeee8 8  88 8  8  8 8  88 8   8 8  88 8   8  8  88 
8eee8 8eeee8 88     8   8 8e 8  8 8   8 8e  8 8   8 8eee8e 8   8 
88      88   88     8   8 88 8  8 8   8 88  8 8   8 88   8 8   8 
88      88   88     8eee8 88 8  8 8eee8 88ee8 8eee8 88   8 8eee8 

    """)

# déclarations des variables
etude = int(input("vous voulez étudier pour combien de minutes?"))
pause = int(input("combien de temps pour les pause?"))

# variable affiché par l'apps
minuteEtude = etude - 1 # je vais jamais étudier 1 min
seconde = 60
minutePause = pause - 1

# convertir minutes en seconde
minutes_en_seconde_etude = minuteEtude * 60
minutes_en_seconde_pause = minutePause * 60

# condition de sortie
autrePomodoro = True

# boucle de l'apps
while(autrePomodoro):

    # boucle d'étude
    for i in range(minutes_en_seconde_etude):
        time.sleep(1)
        seconde = seconde - 1
        if (seconde == 0):
            seconde = 60
            minuteEtude = minuteEtude - 1
        os.system('clear')
        print(f"{minuteEtude}:{seconde} d'Études ")
    print(f"pause de {pause} minutes")
    # boucle de pause
    for i in range(minutes_en_seconde_pause):
        time.sleep(1)
        seconde = seconde - 1
        if (seconde == 0):
            seconde = 60
            minutePause = minutePause - 1
        os.system('clear')
        print(f"{minutePause}:{seconde} de pause")
    
    # demande de sortie
    sortie = input("Voulez-vous faire un autre pomodoro?(y/n)")
    if (sortie == 'n' or sortie == 'N'):
        autrePomodoro = False
        
