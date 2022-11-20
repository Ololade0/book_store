# Generated by Django 4.1.3 on 2022-11-20 18:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(5, 'code must be greater than five'), django.core.validators.MaxLengthValidator(6, 'code cannot exceed the length six')])),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='-')),
                ('isbn', models.CharField(max_length=20)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_published', models.DateField()),
                ('edition', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('genre', models.CharField(choices=[('C', 'Comedy'), ('T', 'Tragedy'), ('TC', 'Tragicomedy'), ('CR', 'Crime'), ('R', 'Romance'), ('SF', 'Science Fiction')], default='R', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
    ]
