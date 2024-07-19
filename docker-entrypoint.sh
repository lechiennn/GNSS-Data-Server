#!/bin/sh

# Wait for the database to be ready
echo "Waiting for database..."

until mysqladmin ping -h"$DB_HOST" -P"$DB_PORT" -u"$DB_USER" -p"$DB_PASSWORD" --silent; do 
  echo "Database is not ready, waiting..."
  sleep 1
done

echo "Database is up - continuing..."

python manage.py collectstatic

# Execute the command passed to the entrypoint (e.g., uwsgi --ini uwsgi.ini)
exec "$@"