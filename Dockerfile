FROM ubuntu:latest
RUN mkdir /code
EXPOSE 80
ENV OCAMLSPEED_DB_LOCATION /db/data.db
WORKDIR /code
COPY . /code/
RUN apt-get update && apt-get install -y nginx python3 python3-pip gettext-base
RUN pip3 install --upgrade pip
RUN pip3 install -e . && pip3 install uwsgi
RUN mv ocamlspeed/deploy/nginx.default-site.conf /etc/nginx/sites-enabled/default
CMD ./prepare_and_start.sh
