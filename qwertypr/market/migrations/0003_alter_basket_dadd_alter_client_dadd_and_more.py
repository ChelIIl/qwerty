# Generated by Django 4.0.1 on 2022-01-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='dadd',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='dadd',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dadd',
            field=models.DateField(auto_now_add=True),
        ),
    ]
