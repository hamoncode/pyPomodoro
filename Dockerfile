FROM python:latest

ADD main.py .

RUN pip install pygame

CMD ["python", "./main.py"]


