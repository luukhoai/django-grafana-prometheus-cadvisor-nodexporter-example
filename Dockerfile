FROM python:3.5.2-onbuild
#RUN apt-get update && apt-get install nodejs -y
EXPOSE 8000
#CMD python manage.py runserver 0:8000
CMD [ "sh", "./all_run.sh" ]