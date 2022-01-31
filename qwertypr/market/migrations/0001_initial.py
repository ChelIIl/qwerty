# Generated by Django 4.0.1 on 2022-01-28 11:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dadd', models.DateField(default=datetime.datetime.now)),
                ('name', models.TextField()),
                ('login', models.TextField(max_length=20)),
                ('passwort', models.TextField(max_length=10)),
                ('balance', models.FloatField()),
                ('adress', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField(blank=True, max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dadd', models.DateField(default=datetime.datetime.now)),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('desc', models.TextField()),
                ('available', models.BooleanField(default=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dadd', models.DateField(default=datetime.datetime.now)),
                ('count', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.product')),
            ],
        ),
    ]
