<div align="center">
	<h1>🚀 Telegram Parser Pro</h1>
	<p>
		<strong>Мощный инструмент для работы с Telegram API</strong>
	</p>
	<p>
		<a href="#особенности">Особенности</a> •
		<a href="#установка">Установка</a> •
		<a href="#использование">Использование</a> •
		<a href="#api">API</a> •
		<a href="#лицензия">Лицензия</a>
	</p>

	[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
	[![Flask Version](https://img.shields.io/badge/flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
	[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
</div>

## 📋 Особенности

### 🔍 Глобальный поиск
- Поиск по каналам, чатам и ботам
- Фильтрация по количеству участников
- Поиск по названию, описанию и юзернейму
- Экспорт результатов в CSV/TXT/DOCX

### 📊 Парсинг каналов
- Гибкая настройка параметров парсинга
- Фильтрация по дате и ключевым словам
- Поддержка медиафайлов и пересылаемых сообщений
- Отслеживание прогресса в реальном времени

### 📬 Массовая рассылка
- Отправка сообщений группам пользователей
- Поддержка медиафайлов и форматирования
- Настраиваемые задержки между отправками
- Inline-кнопки и превью ссылок

## 🚀 Установка

1. **Клонирование репозитория**
```bash
git clone https://github.com/swensi17/tgpars.git
cd tgpars
```

2. **Создание виртуального окружения**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Установка зависимостей**
```bash
pip install -r requirements.txt
```

4. **Настройка конфигурации**
```bash
cp .env.example .env
# Отредактируйте .env файл, добавив свои API ключи
```

5. **Инициализация базы данных**
```bash
python init_db.py
```

## 💻 Использование

### Запуск приложения
```bash
python app.py
```
Приложение будет доступно по адресу: http://localhost:5000

### Авторизация
1. Войдите через Telegram
2. Введите код подтверждения
3. При необходимости пройдите двухфакторную аутентификацию

## 🛠 API

### Глобальный поиск
```python
GET /global_search
POST /global_search
```

### Парсинг каналов
```python
GET /parse_channel
POST /parse_channel
```

### Массовая рассылка
```python
GET /send_message
POST /send_message
```

## ⚙️ Конфигурация

### Параметры .env файла
```env
FLASK_SECRET_KEY=your-secret-key
TELEGRAM_API_ID=your-api-id
TELEGRAM_API_HASH=your-api-hash
```

## 📝 Требования

- Python 3.8+
- Flask 2.3.3+
- Telethon 1.29.2+
- SQLite3

## 🔒 Безопасность

- Не публикуйте файл .env
- Храните сессии в безопасном месте
- Регулярно обновляйте зависимости

## 🤝 Вклад в проект

Мы приветствуем ваш вклад в развитие проекта! Для этого:
1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Отправьте пулл-реквест

## 📄 Лицензия

MIT License © [swensi]

## 🙏 Благодарности

- [Telethon](https://github.com/LonamiWebs/Telethon)
- [Flask](https://flask.palletsprojects.com/)
- [Python](https://www.python.org/)

---

<div align="center">
	<sub>Built with ❤️ by swensi</sub>
</div>