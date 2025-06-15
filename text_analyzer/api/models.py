import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

# Расширенный пользователь
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username

# Документ
class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

# Коллекция документов
class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=255)
    documents = models.ManyToManyField(Document, related_name='collections')

    def __str__(self):
        return self.name

# Статистика слов (по документу или коллекции)
class Statistics(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='statistics')
    word = models.CharField(max_length=255)
    tf = models.FloatField()
    idf = models.FloatField()

    def __str__(self):
        return f"{self.word}: TF={self.tf}, IDF={self.idf}"

