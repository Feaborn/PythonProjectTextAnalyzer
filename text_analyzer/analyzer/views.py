from django.shortcuts import render
from .forms import DocumentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import math
from collections import defaultdict
import re
from django.conf import settings
import os
from .models import Document, Metric
from django.http import JsonResponse


def clean_text(text):
    """
    Очищает текст от лишних символов.
    Удаляет все, кроме букв и пробелов, приводит к нижнему регистру.
    - re.sub() эффективнее цепочки replace()
    - lower() обеспечивает регистронезависимый анализ
    - Сохраняет только \w (буквы/цифры) и \s (пробелы)
    """
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text


def compute_tf(text):
    """
    Вычисляет Term Frequency (TF) - частоту термина в документе.
    - defaultdict автоматически инициализирует нулевые значения
    - Абсолютная частота -> относительная (нормализация)
    - Сложность O(n), где n - количество слов
    """
    words = text.split()
    total_words = len(words)
    tf = defaultdict(int)  # Автоинициализация нулем при обращении к новому ключу

    # Подсчет абсолютной частоты
    for word in words:
        tf[word] += 1

    # Преобразование в относительную частоту
    for word in tf:
        tf[word] = tf[word] / total_words  # [0, 1]

    return tf


def compute_idf(documents):
    """
    Вычисляет Inverse Document Frequency (IDF).
    - Показывает редкость слова в коллекции документов
    - Формула: log(общее_число_документов / документы_содержащие_слово)
    - seek(0) важен для последующих чтений файла
    """
    idf = defaultdict(float)
    total_documents = len(documents)

    for doc in documents:
        # set() для уникальных слов в документе
        unique_words = set(clean_text(doc.read().decode('utf-8')).split())
        for word in unique_words:
            idf[word] += 1
        doc.seek(0)  # Сброс позиции файла для будущих операций

    # Расчет IDF с защитой от деления на ноль
    for word in idf:
        idf[word] = math.log(total_documents / (idf[word]))

    return idf


def upload_file(request):
    """
    Обрабатывает загрузку файлов и расчет TF-IDF.
    1. Разделение GET/POST обработки
    2. ModelForm сохраняет файл в MEDIA_ROOT автоматически
    3. Поток обработки: загрузка -> очистка -> TF -> IDF -> сортировка
    4. Безопасность: is_valid() проверяет файл
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_doc = form.save()  # Автоматическое сохранение в БД и MEDIA_ROOT

            # Получаем все документы для расчета IDF
            documents = Document.objects.all()
            document_files = [doc.file for doc in documents]

            # Чтение и обработка текущего файла
            current_file = new_doc.file
            text = current_file.read().decode('utf-8')
            cleaned_text = clean_text(text)

            # Вычисление метрик
            tf = compute_tf(cleaned_text)
            idf = compute_idf(document_files)

            # Формирование результатов
            results = []
            for word in tf:
                results.append({
                    'word': word,
                    'tf': tf[word],  # Term Frequency
                    'idf': idf.get(word, 0),  # Inverse Document Frequency
                })

            # Сортировка по IDF (по убыванию) и выбор топ-50
            sorted_results = sorted(results,
                                 key=lambda x: x['idf'],
                                 reverse=True)[:50]

            return render(request, 'analyzer/results.html', {'results': sorted_results})
    else:
        form = DocumentForm()  # Пустая форма для GET-запроса

    return render(request, 'analyzer/upload.html', {'form': form})

def metrics_view(request):
    latest = Metric.objects.order_by('-timestamp').first()
    if not latest:
        data = {"files_uploaded": 0, "unique_words_analyzed": 0}
    else:
        data = {
            "files_uploaded": latest.files_uploaded,
            "unique_words_analyzed": latest.unique_words_analyzed,
        }
    return JsonResponse(data)