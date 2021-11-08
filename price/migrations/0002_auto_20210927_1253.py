# Generated by Django 3.2.7 on 2021-09-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricechanged',
            name='price_text_1',
            field=models.CharField(max_length=50, verbose_name='Название первого текста'),
        ),
        migrations.AlterField(
            model_name='pricechanged',
            name='price_text_2',
            field=models.CharField(max_length=50, verbose_name='Название второго текста'),
        ),
        migrations.AlterField(
            model_name='pricechanged',
            name='price_text_3',
            field=models.CharField(max_length=50, verbose_name='Название третьего текста'),
        ),
        migrations.AlterField(
            model_name='pricechanged',
            name='price_text_4',
            field=models.CharField(max_length=50, verbose_name='Название четвёртого текста'),
        ),
        migrations.AlterField(
            model_name='pricechanged',
            name='price_text_5',
            field=models.CharField(max_length=50, verbose_name='Название пятого текста'),
        ),
    ]
