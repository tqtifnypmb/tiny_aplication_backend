FROM python:2.7-slim
WORKDIR /usr/app
COPY . /usr/app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV=development
CMD ["sh", "setup.sh"]
