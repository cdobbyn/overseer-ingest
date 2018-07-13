#!/bin/bash

echo "Starting in ${PWD}"

VENV_BIN=/opt/venv/bin

args="$@"

case $1 in
    python)
        exec ${VENV_BIN}/python ${@:2}
        ;;
    ingest)
        ${VENV_BIN}/python manage.py collectstatic --noinput
        exec ${VENV_BIN}/uwsgi --module=app.wsgi:application \
                   --master \
                   --http 0.0.0.0:8000 \
                   --harakiri=60 \
                   --max-requests=1000 \
                   --processes=4 \
                   --vacuum
        ;;
    uwsgi-dev)
        exec ${VENV_BIN}/uwsgi --module=app.wsgi:application \
                   --http 0.0.0.0:8000 \
                   --master \
                   --processes=1 \
                   --py-autoreload=2
        ;;
    runserver)
        exec $VENV_BIN/python manage.py runserver 0.0.0.0:8000
        ;;
    test)
        $VENV_BIN/python manage.py collectstatic --noinput
        exec $VENV_BIN/python manage.py test lantasy --noinput
        ;;
    *)
        exec "$@"
        ;;
esac