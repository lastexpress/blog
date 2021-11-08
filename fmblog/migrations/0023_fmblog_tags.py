# Generated by Django 3.2.7 on 2021-10-19 10:23

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('fmblog', '0022_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmblog',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
