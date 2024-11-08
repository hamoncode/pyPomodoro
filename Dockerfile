FROM python:latest

ADD main.py .

RUN pip install pygame tqdm

CMD ["python", "./main.py"]


