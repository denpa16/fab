# Generated by Django 2.2 on 2021-12-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_answer_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
