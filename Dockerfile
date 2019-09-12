FROM python:3.7.4-alpine3.10

WORKDIR /usr/local/app

COPY *.py ./

CMD ["python", "main.py"]