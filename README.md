# pyPomodoro

![image](./image/snapshot.png)

## navigation du projet

### main.py

main apps: python3 main.py

### modules.py

fonctions utilisés dans main.py

#### packages python utilisés
- alarme = pygame
- progressbar = tqdm

### Dockerfile

attempt de runner l'application dans un docker container

BUG: pas reussi a jouer le son mais le container fonctionne sans son:
```bash
docker pull hamoncode/pymodoro:3.0
docker run -it hamoncode/pymodoro:3.0
```

### alarmSound

document avec ficher de son d'alarme en format .wav


