# Telegram Forum Bot

Веб-приложение на Flask для работы с Telegram API. Позволяет управлять каналами, чатами и ботами через веб-интерфейс.

## Функциональность

- Авторизация через Telegram
- Глобальный поиск по каналам, чатам и ботам
- Парсинг сообщений из каналов
- Массовая рассылка сообщений
- Управление подписками

## Установка и настройка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/telegram-forum.git
cd telegram-forum
```

2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
pip install -r requirements.txt
```

3. Создайте файл .env в корневой директории проекта:
```
FLASK_SECRET_KEY=ваш-секретный-ключ
TELEGRAM_API_ID=ваш-api-id
TELEGRAM_API_HASH=ваш-api-hash
```

4. Инициализируйте базу данных:
```bash
python init_db.py
```

5. Запустите приложение:
```bash
python app.py
```

Приложение будет доступно по адресу http://localhost:5000

## Получение API ключей Telegram

1. Перейдите на https://my.telegram.org/auth
2. Войдите в свой аккаунт
3. Перейдите в "API development tools"
4. Создайте новое приложение
5. Скопируйте API_ID и API_HASH в файл .env

## Структура проекта

- `app.py` - основной файл приложения
- `init_db.py` - скрипт инициализации базы данных
- `schema.sql` - схема базы данных
- `templates/` - HTML шаблоны
- `static/` - статические файлы (CSS, JavaScript)
- `sessions/` - сессии Telegram (создается автоматически)
- `uploads/` - временные файлы для загрузки (создается автоматически)

## Безопасность

- Не публикуйте файл .env
- Не загружайте в репозиторий файлы сессий (.session)
- Не публикуйте базу данных (database.db)