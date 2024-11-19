# Используем образ Python
FROM python:3.13

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Настройка переменной окружения для Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Копируем скрипт в контейнер
COPY entrypoint.sh /app/

# Делаем скрипт исполняемым
RUN chmod +x /app/entrypoint.sh

# Указываем точку входа
ENTRYPOINT ["/app/entrypoint.sh"]

# Запускаем сервер при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
