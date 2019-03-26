FROM ubuntu:latest
COPY . /usr/app
WORKDIR /usr/app
RUN apt-get -y update
RUN apt-get install -y python3-pip python3-dev 
RUN ln -s /usr/bin/python3 python
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV=development
CMD ["uwsgi", "--ini", "wsgi.ini"]