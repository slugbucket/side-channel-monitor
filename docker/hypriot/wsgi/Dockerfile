# Pull base image
# Based on local python base image 
#FROM resin/rpi-raspbian:wheezy
FROM localhost/slugbucket:hpyriot-python
MAINTAINER Julian Rawcliffe <julianrawcliffe@gmail.com>

# Install dependencies
RUN apt-get update && \
    apt-get install -y build-essential python-dev && \
    pip install \
    Flask \
    uwsgi \
    requests && \
    apt-get purge --auto-remove build-essential python-dev

# Define working directory
WORKDIR /data

# Define default command
CMD ["bash"]
