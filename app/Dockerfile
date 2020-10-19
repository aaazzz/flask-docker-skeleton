FROM python:3.5

COPY . /app
WORKDIR /app

RUN apt update && apt install -y nginx python-pip rsyslog
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN mv etc/nginx.conf /etc/nginx/nginx.conf
RUN mv etc/uwsgi.ini /etc/uwsgi.ini
RUN mv etc/supervisord.conf /etc/supervisord.conf

EXPOSE 80
CMD ["/usr/local/bin/supervisord"]
