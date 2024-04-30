from rest_framework import serializers
from .models import Document,Text,GroqRes

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('file',)

class TextSerializer(serializers.ModelSerializer):
  class Meta:
    model = Text
    fields = ('')
class GroqResSerializer(serializers.ModelSerializer):
   class Meta:
      model = GroqRes
      fields = ('')