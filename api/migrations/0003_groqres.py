# Generated by Django 5.0.4 on 2024-04-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroqRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
