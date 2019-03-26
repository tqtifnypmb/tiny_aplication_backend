FROM ubuntu:latest
WORKDIR /usr/app
COPY . /usr/app
RUN apt-get -y update
RUN apt-get install -y python3-pip python3-dev 
RUN ln -s /usr/bin/python3 python
RUN pip3 install -i http://mirrors.tencentyun.com/pypi/simple --upgrade pip
RUN pip3 install -i http://mirrors.tencentyun.com/pypi/simple -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV=development
CMD ["uwsgi", "--ini", "wsgi.ini"]