# Generated by Django 3.0 on 2020-10-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201007_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_product',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]
