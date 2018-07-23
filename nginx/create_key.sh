#!/usr/bin/env bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /home/silverlight/Projects/test_django/nginx/nginx.key -out /home/silverlight/Projects/test_django/nginx/nginx.crt