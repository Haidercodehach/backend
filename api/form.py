from django import forms
from .models import Document,Text

class DocumentFrom(forms.ModelForm):
    class Meta:
        modul = Document
        field = ('file',)
class TextFrom(forms.ModelForm):
    class Meta:
        modul = Text
        field = ('text',)