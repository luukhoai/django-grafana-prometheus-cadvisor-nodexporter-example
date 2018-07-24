FROM nginx:1.15.0
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx.crt /etc/nginx/ssl/nginx.crt
COPY nginx.key /etc/nginx/ssl/nginx.key
COPY .htpasswd /etc/nginx/.htpasswd
COPY ./uwsgi_params /etc/nginx/uwsgi_params