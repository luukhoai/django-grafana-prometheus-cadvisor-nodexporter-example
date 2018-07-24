#!/usr/bin/env bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /home/silverlight/Projects/test_django/nginx/nginx.key -out /home/silverlight/Projects/test_django/nginx/nginx.crt


## Create username password
sudo sh -c "echo -n 'admin:' >> /home/silverlight/Projects/test_django/nginx_dashboard/.htpasswd"
sudo sh -c "openssl passwd -apr1 >> /home/silverlight/Projects/test_django/nginx_dashboard/.htpasswd"


### Grafana: username and password need correct with grafana login