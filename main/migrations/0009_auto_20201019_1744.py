# Generated by Django 3.0 on 2020-10-19 11:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201019_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_product',
            field=models.SlugField(default=uuid.uuid1, unique=True, verbose_name='URL'),
        ),
    ]
