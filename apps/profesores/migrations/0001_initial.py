# Generated by Django 3.1.3 on 2020-11-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('last_name', models.CharField(blank=True, max_length=120)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=120)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
                'ordering': ['name'],
            },
        ),
    ]
