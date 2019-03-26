FROM ubuntu:latest
COPY . /usr/app
WORKDIR /usr/app
# COPY ./sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev 
RUN ln -s /usr/bin/python3 python
RUN pip3 install --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV=development
CMD ["uwsgi", "--ini", "wsgi.ini"]