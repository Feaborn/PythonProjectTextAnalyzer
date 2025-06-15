from django.apps import AppConfig

class AnalyzerConfig(AppConfig):
    """
    Конфигурация приложения analyzer.
    Определяет метаданные и поведение приложения.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Тип автоинкрементного поля
    name = 'analyzer'  # Имя приложения (должно совпадать с именем папки)