# image de base
FROM python:latest

# bugfix : driver pygame -> dummy
ENV SDL_AUDIODRIVER=dummy

# cd dans l'application
WORKDIR /app

# ajouter tous les fichiers de l'apps
ADD . .

# ajouter packages qu'on a besoin
RUN pip install pygame tqdm

# lancer l'application
CMD ["python", "./main.py"]


