# Generated by Django 5.0.2 on 2024-03-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sibi',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=12)),
            ],
        ),
    ]
