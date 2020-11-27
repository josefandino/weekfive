# Generated by Django 3.1.3 on 2020-11-27 07:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(4)])),
                ('creditos', models.IntegerField(blank=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('activo', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
                'ordering': ['code'],
            },
        ),
    ]
