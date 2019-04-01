FROM ubuntu
COPY . /usr/local/app
WORKDIR /usr/local/app

RUN apt-get y update
RUN apt-get install python3-pip python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000
ENV FLASK_ENV=development
CMD [ "uwsgi", "--ini", "wsgi.ini" ]