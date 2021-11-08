# Generated by Django 3.2.7 on 2021-10-11 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmblog', '0019_auto_20211011_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmblog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fmblog.categorylist'),
        ),
        migrations.AlterField(
            model_name='categorylist',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fmblog.fmblog'),
        ),
    ]
