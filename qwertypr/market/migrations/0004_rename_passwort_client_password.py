# Generated by Django 4.0.1 on 2022-01-31 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_alter_basket_dadd_alter_client_dadd_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='passwort',
            new_name='password',
        ),
    ]
