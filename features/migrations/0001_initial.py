# Generated by Django 3.2.7 on 2021-09-23 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fts_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('fts_desc', models.TextField(verbose_name='Описание')),
                ('fts_img', models.ImageField(upload_to='sliderimg/')),
            ],
            options={
                'verbose_name': 'Функция',
                'verbose_name_plural': 'Функции',
            },
        ),
    ]
