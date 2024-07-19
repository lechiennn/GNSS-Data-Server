FROM python:3.8

WORKDIR /app

RUN apt update && apt install -y \
    build-essential \
    libpq-dev \
    mariadb-client \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN chmod +x /app/docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]

CMD ["uwsgi", "--ini", "uwsgi.ini"]