FROM python

WORKDIR /opt/app-web-docker

RUN  mkdir -p /opt/app-web-docker/data

COPY requirements.txt .
COPY . .

RUN rm docker-compose.yml
RUN rm Dockerfile
RUN rm .env


RUN pip install --no-cache-dir --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
