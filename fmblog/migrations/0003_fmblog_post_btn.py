# Generated by Django 3.2.7 on 2021-09-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmblog', '0002_fmblog_fm_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmblog',
            name='post_btn',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Название кнопки'),
        ),
    ]
