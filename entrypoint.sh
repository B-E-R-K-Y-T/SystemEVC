#!/bin/sh

# Генерация миграций
python manage.py makemigrations

# Запуск миграций
python manage.py migrate

# Запуск сервера
exec "$@"
