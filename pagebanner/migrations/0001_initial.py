# Generated by Django 3.2.7 on 2021-09-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_name', models.CharField(max_length=250, verbose_name='Название главного заголовка')),
                ('banner_btn_1', models.CharField(max_length=250, verbose_name='Название первого раздела')),
                ('banner_btn_2', models.CharField(max_length=250, verbose_name='Название второго раздела')),
                ('banner_btn_3', models.CharField(max_length=250, verbose_name='Название третьего раздела')),
            ],
            options={
                'verbose_name': 'Заголовок баннера',
                'verbose_name_plural': 'Заголовок баннера',
            },
        ),
    ]
