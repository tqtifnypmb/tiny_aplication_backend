FROM mysql/mysql-server

COPY schema.sql /docker-entrypoint-initdb.d

ENV MYSQL_ROOT_HOST=172.*.*.*
ENV MYSQL_USER=suns
ENV MYSQL_DATABASE=suns
ENV MYSQL_PASSWORD=1816400