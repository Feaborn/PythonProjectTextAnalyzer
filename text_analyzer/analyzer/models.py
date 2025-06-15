from django.db import models


class Document(models.Model):
    # FileField: хранение файлов в upload_to + обработка в views
    file = models.FileField(upload_to='documents/')

    # auto_now_add: автоматическая установка времени при создании
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Для отображения объекта в админке и shell
        return self.file.name

class Metric(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    files_uploaded = models.IntegerField(default=0)
    unique_words_analyzed = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.timestamp} | Files: {self.files_uploaded}, Words: {self.unique_words_analyzed}"