# Generated by Django 5.0.3 on 2024-03-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_productreview_product_alter_productreview_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars'), (6, '6 Stars'), (7, '7 Stars')], default=None),
        ),
    ]
