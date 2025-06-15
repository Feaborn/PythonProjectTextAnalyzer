# 🧠 Python Project Text Analyzer

Веб-приложение на Django, позволяющее загружать текстовые файлы, анализировать их с использованием TF-IDF, работать с коллекциями документов и просматривать результаты через Swagger-интерфейс.

---

## 🔧 Структура проекта

```
├── Dockerfile                   # Инструкция сборки контейнера
├── docker-compose.yml          # Docker Compose для PostgreSQL и Django
├── requirements.txt            # Python-зависимости
├── README.md                   # Документация проекта
├── .env.example                # Пример переменных окружения
├── text_analyzer/              # Django-проект
│   ├── manage.py               # Django CLI
│   ├── analyzer/               # Основное приложение
│   │   ├── views.py, forms.py  # Логика и формы
│   │   ├── models.py, serializers.py, urls.py
│   │   └── templates/          # HTML-шаблоны
│   ├── api/                    # Эндпоинты REST API
│   │   ├── views.py, urls.py, serializers.py
│   └── text_analyzer/          # Настройки проекта (settings.py, urls.py)
└── media/documents/            # Хранилище загруженных файлов
```

---

## 🚀 Полный запуск на сервере через Docker Compose

### 📦 1. Перенос проекта на сервер (с локальной машины):

```bash
scp -i "путь_до_ключа" -r ПУТЬ_К_ПРОЕКТУ ubuntu@<IP>:~
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

- Swagger-интерфейс: http://<IP-адрес сервера>:8000/swagger/
- Админка Django: http://<IP-адрес сервера>:8000/admin/

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

## 🖥️ Альтернатива: запуск вручную (без Docker)

```bash
git clone https://github.com/Feaborn/PythonProjectTextAnalyzer.git
cd PythonProjectTextAnalyzer/text_analyzer
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
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