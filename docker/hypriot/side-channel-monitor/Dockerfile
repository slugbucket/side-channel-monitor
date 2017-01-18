 Pull base image
# Based on local python uwsgi image with Flask pip installed
#FROM resin/rpi-raspbian:wheezy
FROM localhost/slugbucket:hypriot-python-wsgi
MAINTAINER Julian Rawcliffe <julianrawcliffe@gmail.com>

# Install application files
ADD side-channel-monitor.py /var/www/uwsgi/flask/side-channel-monitor/side-channel-monitor.py

# Make a port externally available
EXPOSE 7071

# Define working directory
WORKDIR /var/www/uwsgi/flask/side-channel-monitor

# Define default command
CMD ["uwsgi", "--wsgi-file", "/var/www/uwsgi/flask/side-channel-monitor/side-channel.py", "--callable", "app", "--processes", "4", "--threads", "2", "--uid", "nobody", "--gid", "nogroup", "--http", "0.0.0.0:7071", "--logto", "/var/log/side-channel-monitor.log"]
