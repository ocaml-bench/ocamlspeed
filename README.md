# OCamlspeed
[![Build Status](https://cloud.drone.io/api/badges/ocaml-bench/ocamlspeed/status.svg)](https://cloud.drone.io/ocaml-bench/ocamlspeed)

OCamlspeed is a web application to monitor and analyze performance.

The master branch is automatically built as a docker image and published to the [ocamlbench/ocamlspeed](https://hub.docker.com/r/ocamlbench/ocamlspeed) image on docker hub.

To deploy using docker compose, for an environment with a single ocamlspeed running you will need a config that looks like the following:

```
version: '3'

services:
  ocamlspeed_example:
    image: ocamlbench/ocamlspeed
    environment:
      - OCAMLSPEED_HOST=examplespeed.example.com
      - OCAMLSPEED_NAME=example
      - OCAMLSPEED_DESCRIPTION=This is an example ocamlspeed deploy
      - OCAMLSPEED_LOGO=http://www.example.com/example.icon.png
      - OCAMLSPEED_SECRET_KEY=pickarandomsecretkeyherethatsbetterthanthis
      - OCAMLSPEED_NORMALIZE=true
    ports: 
        - "8080:80"
    volumes:
        - "./example-data:/data/"
        - "./example-artifacts:/artifacts/"
```

This assumes you want the example ocamlspeed instance running on port 8080 on the local machine and you have two directories example-data and example-artifacts in the current directory which will be used for the database and run artifacts respectively.

After this you can run ```docker-compose up -d``` to start the environment.
