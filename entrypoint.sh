#!/bin/sh

echo "Aguardando inicilização do postgres..."

while ! nc -z usuarios-db 5432; do
  sleep 0.1
done

echo "PostgreSQL inicializado!"

python manage.py run -h 0.0.0.0