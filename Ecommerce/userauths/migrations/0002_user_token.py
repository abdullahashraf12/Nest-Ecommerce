# Generated by Django 5.0.3 on 2024-03-22 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='', max_length=64, unique=True),
            preserve_default=False,
        ),
    ]