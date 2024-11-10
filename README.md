# pyPomodoro
![image](./image/snapshot.png)

## navigation du projet

### main.py
main apps: python3 main.py

### modules.py
fonctions utilisés dans main.py

<<<<<<< HEAD
=======
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

>>>>>>> e676f3814fce9560e54a1ac02e65c7e61ad549cf
### alarmSound
document avec ficher de son d'alarme en format .wav

### Dockerfile
attempt de runner l'application dans un docker container

BUG:reussi a jouer le son mais seulement avec  un serveur pulseaudio
- sa fonctionnera pas sur windows sans utiliser WSL2

```bash
docker pull hamoncode/pymodoro:4.0

dockerdocker run -it -v /run/user/1000/pulse:/run/user/1000/pulse -e PULSE_SERVER=unix:/run/user/1000/pulse/native --user $(id -u):$(id -g) pymodorobuntu:4.0
```



