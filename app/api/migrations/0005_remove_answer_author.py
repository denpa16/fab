# Generated by Django 2.2 on 2021-12-14 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_answer_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
    ]