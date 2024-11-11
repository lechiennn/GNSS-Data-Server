#!/bin/sh

# Wait for the database to be ready
echo "Waiting for database..."

until pg_isready -h "$DB_HOST" -p "$DB_PORT"; do 
  echo "Database is not ready, waiting..."
  sleep 1
done

echo "Database is up - continuing..."

python manage.py collectstatic --noinput

# Execute the command passed to the entrypoint (e.g., uwsgi --ini uwsgi.ini)
exec "$@"