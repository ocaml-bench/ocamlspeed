FROM ubuntu:latest
RUN apt-get update && apt-get install -y git nginx python3 python3-pip gettext-base
RUN pip3 install --upgrade pip
RUN pip3 install uwsgi
RUN mkdir /code
EXPOSE 80
ENV OCAMLSPEED_DB_LOCATION /data/data.db
WORKDIR /code
COPY . /code/
RUN pip3 install -e .
RUN mv ocamlspeed/deploy/nginx.default-site.conf /etc/nginx/sites-enabled/default
CMD ./prepare_and_start.sh
