# Трекер полезных привычек

Бэкенд‑часть SPA‑приложения для отслеживания привычек, вдохновлённого книгой «Атомные привычки».  
Проект реализован на Django + Django REST Framework с интеграцией Telegram‑бота и отложенными задачами через Celery.

## Основные возможности

- Регистрация и авторизация пользователей (JWT‑токены).
- CRUD для привычек с валидацией бизнес‑правил:
  - Время выполнения ≤ 2 минут.
  - Периодичность от 1 до 7 дней.
  - Запрет одновременного заполнения вознаграждения и связанной привычки.
  - Приятная привычка не может иметь вознаграждения или связанной привычки.
  - Связанная привычка может быть только приятной.
- Пагинация списка привычек (5 на страницу).
- Права доступа: пользователь управляет только своими привычками, публичные привычки доступны на чтение всем.
- Интеграция с Telegram‑ботом для отправки напоминаний о привычках.
- Асинхронная отправка сообщений через Celery (периодическая задача каждую минуту).
- Автоматическое создание периодических задач через `django_celery_beat`.
- Документация API (Swagger / ReDoc).

## Технологии

- Python 3.13
- Django 6.0.6
- Django REST Framework 3.17.1
- Celery 5.6.3 + Redis (брокер)
- django-celery-beat (планировщик)
- django-cors-headers
- drf-yasg (документация)
- PostgreSQL (база данных)
- Requests (отправка в Telegram)

## Установка и запуск

### 1. Установить зависимости с Poetry
```
poetry install
```

### 2. Клонировать репозиторий
```
git clone https://github.com/Margarita2405/Project13_Course_work5_Skypro
cd Project13_Course_work5_Skypro
```
   
### 3. Создать базу данных PostgreSQL

CREATE DATABASE habit_tracker;

### 4. Создать файл .env в корне проекта (по примеру .env.example):

```
SECRET_KEY=your_secret_key_here

DEBUG=True

# НАСТРОЙКИ ПОДКЛЮЧЕНИЯ К PostgreSQL
DATABASE_NAME=habit_tracker
DATABASE_USER=your_user_name
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# GITHUB TOKEN
# Personal Access Token для GitHub
# Создайте на: https://github.com/settings/tokens
# Необходимые scope: repo, read:org, user (в зависимости от нужд)
GITHUB_TOKEN=your_github_token_here

REDIS_URL=redis://localhost:6379/0

TELEGRAM_BOT_TOKEN=your_telegram_token
TELEGRAM_CHAT_ID=your_telegram_id
```

### 5. Создать и применить миграции

```
python manage.py makemigrations
python manage.py migrate
```

### 6. Создать суперпользователя

```
python manage.py createsuperuser
```

### 7. Запуск сервера разработки
```
python manage.py runserver
Проект будет доступен по адресу: http://127.0.0.1:8000
```

### 8. Запустить Redis (должен быть установлен)
```
Windows (WSL): sudo service redis-server start

macOS: brew services start redis

Linux: sudo systemctl start redis-server
```

### 9. Запустить Celery worker и beat (в отдельных терминалах)
```
poetry run celery -A config worker -l INFO --pool=solo
poetry run celery -A config beat -l INFO
```

## Telegram‑бот
- Создайте бота через @BotFather и получите токен.

- Добавьте токен в .env (TELEGRAM_BOT_TOKEN).

- Пользователь должен отправить боту команду /start (чтобы бот мог писать ему).

- В профиле пользователя (админка) укажите telegram_id (число).

- Привычки с временем, совпадающим с текущим, будут отправлять напоминания.

Примечание: Если API Telegram недоступен (блокировка сети), в коде реализована заглушка (логирование в консоль). 
Для реальной работы удалите заглушку в notifications/services.py.

## Запуск тестов
```
python manage.py test
```
Покрытие тестами (≥80%):

```
coverage run manage.py test
coverage report -m
```

## Документация API
- Swagger UI: http://127.0.0.1:8000/swagger/

- ReDoc: http://127.0.0.1:8000/redoc/

## Основные эндпоинты

Метод	         URL	                    Описание
POST	/api/users/register/	    Регистрация пользователя
POST	/api/users/token/	        Получение JWT (access/refresh)
POST	/api/users/token/refresh/	Обновление access‑токена
GET	    /api/habits/	            Список своих привычек (пагинация)
GET	    /api/habits/public/	        Список публичных привычек
POST	/api/habits/	            Создание привычки
GET	    /api/habits/{id}/	        Получение привычки
PUT	    /api/habits/{id}/	        Полное обновление
PATCH	/api/habits/{id}/	        Частичное обновление
DELETE	/api/habits/{id}/	        Удаление

## Админка

Доступна по http://127.0.0.1:8000/admin/.
В админке можно управлять пользователями, привычками, а также настраивать периодические задачи (через Periodic tasks).

## Документация:

Для получения дополнительной информации обратитесь 
к [документации](README.md).

## Лицензия

Проект выполнен в рамках курсовой работы. Свободное использование только в учебных целях.

## Контакты
Разработчик: Буршева Маргарита

Email: mbursheva@mail.ru

Проект: https://github.com/Margarita2405/Project13_Course_work5_Skypro
