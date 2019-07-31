cp /code/ocamlspeed/templates/about.html /tmp/about.html && envsubst < /tmp/about.html > /code/ocamlspeed/templates/about.html && rm /tmp/about.html
cp /code/ocamlspeed/templates/codespeed/base_site.html /tmp/base_site.html && envsubst < /tmp/base_site.html > /code/ocamlspeed/templates/codespeed/base_site.html && rm /tmp/base_site.html
/etc/init.d/nginx start
python3 /code/manage.py migrate
uwsgi --chdir=/code --module=ocamlspeed.deploy.wsgi:application --env=DJANGO_SETTINGS_MODULE=ocamlspeed.settings --master --http=0.0.0.0:49152 --pidfile=/tmp/uwsgi.pid --max-requests=5000 --processes=3
