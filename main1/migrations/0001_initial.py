# Generated by Django 5.0 on 2023-12-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]
