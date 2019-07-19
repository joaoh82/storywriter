FROM python:3.7-alpine

LABEL MAINTAINER="Joao Henrique Machado Silva"
LABEL EMAIL="joaoh82@gmail.com"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY app.py /app

# ENTRYPOINT [ "python" ]

# CMD [ "app.py" ]