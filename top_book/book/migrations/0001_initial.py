# Generated by Django 3.2 on 2021-04-15 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('store_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='', null=True, upload_to='store_image/')),
                ('fav', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
