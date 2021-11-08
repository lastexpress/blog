# Generated by Django 3.2.7 on 2021-09-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bb_btn', models.CharField(max_length=25, verbose_name='Кнопка')),
            ],
            options={
                'verbose_name': 'Кнопка',
                'verbose_name_plural': 'Кнопки',
            },
        ),
        migrations.CreateModel(
            name='BuildWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bw_title', models.CharField(max_length=50, verbose_name='Заголовок bws')),
                ('bw_desc', models.TextField()),
                ('bw_button', models.CharField(max_length=25, verbose_name='Кнопка')),
            ],
            options={
                'verbose_name': 'BuildWs',
                'verbose_name_plural': 'BuildWs',
            },
        ),
    ]