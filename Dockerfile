FROM python:3.8-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV SETTINGS_SECRET_KEY @u0+fivt&8740lo#udvj@$9_2#s8pardnnpnnv(g$0c^#*2scd

COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt

COPY . .

RUN mkdir ../db

COPY ./db.sqlite3 ../db/.

RUN chmod 777 ../db && chmod 777 ../db/db.sqlite3

RUN adduser -D matari
USER matari


