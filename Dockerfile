# Используем базовый образ Python
FROM python:3.9

# Устанавливаем переменные окружения для удобства
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем и переходим в рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Копируем все остальные файлы проекта в контейнер
COPY . .

# Команда для запуска приложения (предполагается, что ваше приложение находится в main.py)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
