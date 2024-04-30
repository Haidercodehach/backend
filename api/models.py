from django.db import models
import os

from groq import Groq
class Document(models.Model):
    file = models.FileField(upload_to='documents/')
class Text(models.Model):
    text = models.TextField()
class GroqRes(models.Model):
    text = models.TextField()
def SendMessage(text):
    os.environ['GROQ_API_KEY'] = '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'
    client = Groq()
    tests = text

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": tests,
            }
        ],
        model="mixtral-8x7b-32768",
    )

    return chat_completion.choices[0].message.content