FROM python:latest

RUN mkdir /app

WORKDIR /app

COPY ./ /app

RUN pip3 install -r requirements-dev.txt

EXPOSE 5000

CMD python3 -m app.app
