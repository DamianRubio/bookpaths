# Generated by Django 3.1.7 on 2021-03-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookpaths_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
