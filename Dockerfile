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

# collect static files
RUN python3 manage.py collectstatic --noinput
RUN chmod 777 ../db && chmod 777 ../db/db.sqlite3

RUN adduser -D matari
USER matari

COPY .env .
CMD source .env && echo $SETTINGS_SECRET_KEY && gunicorn fb_bot.wsgi:application --bind 0.0.0.0:$PORT


