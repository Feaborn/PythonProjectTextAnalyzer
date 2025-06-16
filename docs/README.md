# 🧠 Python Project Text Analyzer

Веб-приложение на Django, позволяющее загружать текстовые файлы, анализировать их с использованием TF-IDF, работать с коллекциями документов и просматривать результаты через Swagger-интерфейс.

---

## 🔧 Структура проекта

```
text_analyzer/                # Корневой Django-проект
├── analyzer/                   # Логика TF-IDF и работы с документами
│   ├── migrations/             # Django-миграции
│   ├── templates/              # (не используется, но включено Django'ом)
│   ├── __init__.py             # Делает папку пакетом
│   ├── admin.py                # Регистрация моделей в админке
│   ├── apps.py                 # Конфигурация приложения
│   ├── forms.py                # Не используется, можно удалить
│   ├── models.py               # Модель Document
│   ├── tests.py                # Тесты приложения
│   ├── urls.py                 # URL-роутинг приложения
│   └── views.py                # Представления (анализ TF-IDF, работа с документами)

├── api/                        # REST API, сериализаторы, авторизация
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── authentication.py       # JWT-аутентификация и регистрация
│   ├── models.py               # Модель Collection и DocumentCollection
│   ├── serializers.py          # Сериализаторы для API: Document, Collection
│   ├── permissions.py          # Кастомные разрешения (доступ к своим объектам)
│   ├── utils.py                # Вспомогательные функции (например, алгоритм Хаффмана)
│   ├── views.py                # ViewSet'ы для всех API-эндпоинтов
│   ├── urls.py                 # Роутинг API
│   └── tests.py

├── text_analyzer/              # Настройки Django
│   ├── __init__.py
│   ├── settings.py             # Все настройки проекта
│   ├── urls.py                 # Глобальный роутинг
│   ├── asgi.py, wsgi.py        # Точки входа сервера (ASGI / WSGI)

├── media/                      # Папка для загружаемых файлов

├── manage.py                   # Django CLI

 docker-compose.yml           # Контейнеризация проекта
 Dockerfile                   # Сборка web-контейнера
 requirements.txt             # Зависимости
```

---

## 🚀 Полный запуск на сервере через Docker Compose

### 📦 1. Перенос проекта на сервер (с локальной машины) и подключение к серверу:

```bash
scp -i "путь_до_ключа" -r ПУТЬ_К_ПРОЕКТУ ubuntu@<IP>:~
ssh ubuntu@37.9.53.151 -i ПУТЬ_К_КЛЮЧУ

```

### 🔧 2. Установка Docker и Docker Compose на сервере (Ubuntu 22.04+)

```bash
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker

# Установка docker compose plugin
sudo apt install docker-compose-plugin
```

Проверь работоспособность:
```bash
docker compose version
```

---

### 🏗 3. Сборка и запуск контейнеров

Перейди в директорию с `docker-compose.yml`:

```bash
cd ~/PythonProjectTextAnalyzer/text_analyzer
```

Собери и запусти проект:

```bash
sudo docker compose up --build
```

---

### 🌐 4. Доступ к приложению

- Приложение: http://37.9.53.151:8000/
- Swagger-интерфейс: http://37.9.53.151:8000/swagger/
- Админка Django: http://37.9.53.151:8000/admin/

---

### 🛠 Возможные проблемы

- ❗ Если порт 8000 занят:
  ```bash
  sudo lsof -i :8000
  sudo kill -9 <PID>
  ```

- ❗ Если контейнер не запускается:
  ```bash
  sudo docker compose down
  sudo docker compose up --build
  ```

---

## 🖥️ Альтернатива: запуск вручную (без ВМ)

```bash
# 1. Клонируем репозиторий
git clone https://github.com/Feaborn/PythonProjectTextAnalyzer.git
cd PythonProjectTextAnalyzer/text_analyzer

# 2. Убедимся, что Docker установлен
docker --version
docker compose version

# 3. Собираем и запускаем контейнеры
docker compose up --build -d

# 4. Выполняем миграции внутри контейнера
docker compose exec web python manage.py migrate

# 5. (По желанию) создаём суперпользователя для доступа к админке
docker compose exec web python manage.py createsuperuser

# 6. Готово! Приложение будет доступно по адресу:
# http://localhost:8000/
# http://localhost:8000/admin/
# http://localhost:8000/swagger/
```

---

## ⚙️ Переменные окружения (`.env`)

```env
APP_PORT=8000
DEBUG=True

POSTGRES_DB=tfidf_db
POSTGRES_USER=tfidf_user
POSTGRES_PASSWORD=strongpassword
DB_HOST=db
DB_PORT=5432
```

---

## 📦 Версия приложения

**v1.2.0**

---

## 📝 Changelog

### v1.2.0

- Все API-эндпоинты реализованы
- Swagger доступен
- Поддержка нескольких коллекций на документ
- Аутентификация и регистрация
- Полная поддержка Docker + деплой на ВМ
- Обновлён README

### v1.1.0

- Docker и .env конфигурация
- Пример переменных окружения

### v1.0.0

- Анализ TF-IDF с загрузкой файлов