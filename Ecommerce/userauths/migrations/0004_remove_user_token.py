# Generated by Django 5.0.3 on 2024-03-22 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_alter_user_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
    ]
