# Generated by Django 3.2.7 on 2021-09-30 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmblog', '0014_categorylist_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fmblog',
            old_name='category_list',
            new_name='category',
        ),
    ]