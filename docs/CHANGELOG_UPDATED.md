# CHANGELOG

## Версия 1.0.0

### Реализованные эндпоинты:

#### Работа с пользователями:
- `POST /register/` — регистрация нового пользователя.
- `POST /login/` — вход в систему (получение токена).
- `POST /logout/` — выход из системы.
- `POST /change-password/` — смена пароля.
- `DELETE /delete-account/` — удаление аккаунта.

#### Работа с документами:
- `POST /documents/` — загрузка нового документа (только `.txt`).
- `GET /documents/` — получение списка всех документов текущего пользователя.
- `GET /documents/<id>/` — просмотр содержимого документа по ID.
- `DELETE /documents/<id>/` — удаление документа по ID.

#### Работа с коллекциями:
- `POST /collections/` — создание новой коллекции.
- `GET /collections/` — просмотр списка коллекций пользователя.
- `GET /collections/<id>/` — просмотр документов внутри коллекции.
- `POST /collections/<collection_id>/add_document/` — добавление документа в коллекцию.
- `POST /collections/<collection_id>/remove_document/` — удаление документа из коллекции.
- `DELETE /collections/<id>/` — удаление коллекции.

#### TF-IDF:
- `GET /documents/<id>/tf-idf/` — получение TF-IDF статистики по отдельному документу.
- `GET /collections/<id>/tf-idf/` — получение TF-IDF статистики по коллекции.

#### Дополнительные алгоритмы:
- `GET /documents/<id>/huffman/` — получение сжатого представления текста с использованием алгоритма Хаффмана.

### Особенности:
- Все запросы, кроме регистрации и логина, требуют авторизации по токену.
- Документ может принадлежать сразу нескольким коллекциям.
- Swagger доступен по адресу: `/swagger/`