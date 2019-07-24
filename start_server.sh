/etc/init.d/nginx start
uwsgi --chdir=/code --module=ocamlspeed.deploy.wsgi:application --env=DJANGO_SETTINGS_MODULE=ocamlspeed.settings --master --http=0.0.0.0:49152 --pidfile=/tmp/uwsgi.pid --max-requests=5000 --processes=10
