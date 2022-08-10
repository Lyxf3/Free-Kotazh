#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

[ -d ./allstaticfiles/static ] || mkdir -p ./allstaticfiles/static
[ -d ./media ] || mkdir ./media

python manage.py makemigrations --noinput --merge
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compilemessages

exec "$@"