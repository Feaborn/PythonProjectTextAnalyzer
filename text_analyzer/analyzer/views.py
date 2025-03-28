from django.shortcuts import render
from .forms import DocumentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import math
from collections import defaultdict
import re
from django.conf import settings
import os
from .models import Document


def clean_text(text):
    # Удаляем все кроме букв и пробелов
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text


def compute_tf(text):
    words = text.split()
    total_words = len(words)
    tf = defaultdict(int)

    for word in words:
        tf[word] += 1

    # Преобразуем в относительные частоты
    for word in tf:
        tf[word] = tf[word] / total_words

    return tf


def compute_idf(documents):
    idf = defaultdict(float)
    total_documents = len(documents)

    for doc in documents:
        unique_words = set(clean_text(doc.read().decode('utf-8')).split())
        for word in unique_words:
            idf[word] += 1
        doc.seek(0)  # Возвращаем указатель в начало файла

    for word in idf:
        idf[word] = math.log(total_documents / (idf[word]))

    return idf


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_doc = form.save()

            # Получаем все документы для IDF
            documents = Document.objects.all()
            document_files = [doc.file for doc in documents]

            # Обрабатываем текущий файл
            current_file = new_doc.file
            text = current_file.read().decode('utf-8')
            cleaned_text = clean_text(text)

            tf = compute_tf(cleaned_text)
            idf = compute_idf(document_files)

            # Собираем результаты
            results = []
            for word in tf:
                results.append({
                    'word': word,
                    'tf': tf[word],
                    'idf': idf.get(word, 0),
                })

            # Сортируем по убыванию IDF и берем топ 50
            sorted_results = sorted(results, key=lambda x: x['idf'], reverse=True)[:50]

            return render(request, 'analyzer/results.html', {'results': sorted_results})
    else:
        form = DocumentForm()

    return render(request, 'analyzer/upload.html', {'form': form})