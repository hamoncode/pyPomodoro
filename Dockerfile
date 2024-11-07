FROM python:latest

ADD main.py .

RUN pip install playsound

CMD ["python", "./main.py"]


