# Generated by Django 3.2.7 on 2021-09-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloges', '0003_auto_20210928_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changefootergallery',
            name='footer_right_title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Заголовок справа'),
        ),
    ]
