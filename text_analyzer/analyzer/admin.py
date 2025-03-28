from django.contrib import admin
from .models import Document

@admin.register(Document)  # Декоратор регистрирует модель
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at')  # Какие поля показывать в списке
    search_fields = ('file',)  # По каким полям можно искать
    list_filter = ('uploaded_at',)  # фильтрация по дате
    readonly_fields = ('uploaded_at',)  # Запретить редактирование даты