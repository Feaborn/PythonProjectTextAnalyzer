# Generated by Django 5.1.7 on 2025-06-01 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('files_uploaded', models.IntegerField(default=0)),
                ('unique_words_analyzed', models.IntegerField(default=0)),
            ],
        ),
    ]
