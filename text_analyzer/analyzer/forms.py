from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    # ModelForm автоматически строит форму по модели
    class Meta:
        model = Document
        fields = ('file',)  # Только поле file

        # Важно: запятая для кортежа из одного элемента!