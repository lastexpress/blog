# Generated by Django 3.2.7 on 2021-09-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildws', '0002_remove_buildwebsite_bw_button'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=20, verbose_name='Название картинки')),
                ('main_img', models.ImageField(upload_to='BuildWs')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
