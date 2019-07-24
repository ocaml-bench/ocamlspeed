FROM ubuntu:latest
RUN mkdir /code
EXPOSE 49152
WORKDIR /code
COPY . /code/
RUN apt-get update && apt-get install -y nginx python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -e . && pip3 install uwsgi
CMD [ "uwsgi", "--chdir=/code", "--module=ocamlspeed.deploy.wsgi:application", "--env=DJANGO_SETTINGS_MODULE=ocamlspeed.settings", "--master", "--http=0.0.0.0:49152", "--pidfile=/tmp/uwsgi.pid", "--max-requests=5000", "--processes=10"]
