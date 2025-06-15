from django.contrib import admin
from .models import Document


@admin.register(Document)  # Регистрация модели в админке через декоратор
class DocumentAdmin(admin.ModelAdmin):
    # list_display - поля для отображения в списке объектов
    # Ошибка E108: если указан несуществующий метод/поле
    list_display = ('id', 'file', 'uploaded_at')

    # search_fields - по каким полям работает поиск
    search_fields = ('file',)  # Запятая важна для кортежа из одного элемента

    # list_filter - боковая панель фильтрации
    list_filter = ('uploaded_at',)

    # readonly_fields - запрет редактирования полей
    readonly_fields = ('uploaded_at',)