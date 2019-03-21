FROM ubuntu:latest
WORKDIR /usr/app
COPY . /usr/app
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev 
RUN ln -s /usr/bin/python3 python
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV=development
CMD ["uwsgi", "--ini", "wsgi.ini"]