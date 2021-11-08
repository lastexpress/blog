# Generated by Django 3.2.7 on 2021-09-30 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmblog', '0005_changetitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True)),
                ('fmblog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='fmblog.fmblog')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]