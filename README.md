# OCamlspeed
[![Build Status](https://cloud.drone.io/api/badges/ocaml-bench/ocamlspeed/status.svg)](https://cloud.drone.io/ocaml-bench/ocamlspeed)

OCamlspeed is a web application to monitor and analyze performance.

The master branch is automatically built as a docker image and published to the [ocamlbench/ocamlspeed](https://hub.docker.com/r/ocamlbench/ocamlspeed) image on docker hub.

To deploy using docker compose, for an environment with a single ocamlspeed running you will need to create a `docker-compose.yml` file that looks like the following:

```
version: '3'

services:
  ocamlspeed_example:
    image: ocamlbench/ocamlspeed
    environment:
      - OCAMLSPEED_HOST=examplespeed.example.com
      - OCAMLSPEED_NAME=example
      - OCAMLSPEED_LOGO=http://www.example.com/example.icon.png
      - OCAMLSPEED_SECRET_KEY=pickarandomsecretkeyherethatsbetterthanthis
      - OCAMLSPEED_NORMALIZE=true
      - OCAMLSPEED_ABOUT_THIS_SITE_BLOCK=<p>This is a demo of benchmarks run on various compilers</p>
      - OCAMLSPEED_ABOUT_BENCHMARKS_BLOCK=<p>The benchmarking code can be found <a href="https://a_link_to_somewhere/">here</a>.</p>
      - OCAMLSPEED_ABOUT_MYPROJECT_BLOCK=<p>The compiler code can be found <a href="https://github.com/somewhere">here</a>.</p>
      - OCAMLSPEED_ABOUT_CONTACT_BLOCK=<p>For problems or suggestions about this website write to somebody@somewhere.com</p>
    ports:
        - "8080:80"
    volumes:
        - "./example-data:/data/"
        - "./example-artifacts:/artifacts/"
```

This assumes you want the example ocamlspeed instance running on port 8080 on the local machine and you have two directories example-data and example-artifacts in the current directory which will be used for the database and run artifacts respectively.

The environment variables (`OCAMLSPEED_...`) in the `docker-compose.yml` file allow you to configure various aspects of the site. You can grep the codebase for `OCAMLSPEED_` to find more configuration hooks; for example there are some in `ocamlspeed/settings.py`.

After this you can run ```docker-compose up -d``` to start the environment.

To do local development, you can run ocamlspeed using django's development server as follows:

```
OCAMLSPEED_HOST=anything OCAMLSPEED_NAME=anything OCAMLSPEED_SECRET_KEY=anything OCAMLSPEED_DB_LOCATION=`pwd`/data.db ./manage.py runserver
```
