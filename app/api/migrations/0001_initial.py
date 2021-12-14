# Generated by Django 2.2 on 2021-12-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
            ],
        ),
    ]
