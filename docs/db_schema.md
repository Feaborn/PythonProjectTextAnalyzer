# Структура базы данных

## Пользователь (User)
- **id** (UUID): Уникальный идентификатор пользователя
- **username** (string): Имя пользователя
- **password** (string): Хэшированный пароль

## Документ (Document)
- **id** (UUID): Уникальный идентификатор документа
- **title** (string): Название документа
- **file** (file path): Путь к загруженному текстовому файлу
- **uploaded_at** (datetime): Дата и время загрузки
- **owner** (ForeignKey → User): Владелец документа

## Коллекция (Collection)
- **id** (UUID): Уникальный идентификатор коллекции
- **name** (string): Название коллекции
- **owner** (ForeignKey → User): Создатель коллекции
- **documents** (ManyToMany → Document): Список документов в коллекции

## Статистика (Statistics)
- **id** (UUID): Уникальный идентификатор записи
- **document** (ForeignKey → Document): Документ, к которому относится статистика
- **word** (string): Слово
- **tf** (float): Term Frequency (частота слова в документе)
- **idf** (float): Inverse Document Frequency (обратная частота в рамках коллекции)
