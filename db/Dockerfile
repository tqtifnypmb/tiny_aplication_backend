FROM mysql/mysql-server

COPY schema.sql /docker-entrypoint-initdb.d

ENV MYSQL_ROOT_HOST=172.*.*.*
ENV MYSQL_USER=wishlist
ENV MYSQL_DATABASE=bucket_list
ENV MYSQL_PASSWORD=1816400