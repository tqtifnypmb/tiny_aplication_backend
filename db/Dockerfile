FROM mysql/mysql-server
WORKDIR /usr/app
COPY my.cnf /etc/mysql/my.cnf
COPY . /usr/app
CMD ["sh", "setup.sh"]
