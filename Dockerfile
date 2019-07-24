FROM ubuntu:latest
RUN mkdir /code
EXPOSE 49152
WORKDIR /code
COPY . /code/
RUN apt-get update && apt-get install -y nginx python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -e . && pip3 install uwsgi
RUN mv ocamlspeed/deploy/nginx.default-site.conf /etc/nginx/sites-enabled/default
CMD ./start_server.sh
