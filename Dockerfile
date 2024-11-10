# image de base
# BUG: driver de son
FROM ubuntu:24.10

RUN apt-get update && \
    apt-get install -y pulseaudio &&\
    apt-get install -y python3 python3-pip python3-venv &&\
    apt-get install -y libsdl2-mixer-dev libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

ENV SDL_AUDIODRIVER=pulse

# cd dans l'application
WORKDIR /app

# ajouter tous les fichiers de l'app
COPY . /app

# set up python virtuel env pour pip install packages
RUN python3 -m venv venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install pygame tqdm

# Add the virtual environment's bin directory to PATH
ENV PATH="/app/venv/bin:$PATH"

# lancer pulseaudio et lancer l'application

CMD ["sh", "-c", "pulseaudio --start && python ./main.py"]

