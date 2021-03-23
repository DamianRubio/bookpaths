# Generated by Django 3.1.7 on 2021-03-23 11:28

import bookpaths_app.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookpaths_app', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn_10', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='ISBN-10 length has to be 10', regex='\\w.{10}$')])),
                ('isbn_13', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='ISBN-13 length has to be 13', regex='\\w.{13}$')])),
                ('title', models.CharField(max_length=240)),
                ('author', models.CharField(max_length=240)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=bookpaths_app.models.get_image_path)),
                ('publishers', models.CharField(max_length=240)),
                ('number_of_pages', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=240)),
                ('follow_count', models.PositiveIntegerField(default=0)),
                ('author', models.ManyToManyField(related_name='proposed_paths', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='paths', to='bookpaths_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='BookPathFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(-1, 'Cancelled'), (0, 'Not started'), (1, 'Work in progress'), (2, 'Bookpath completed')], default=0)),
                ('current_step', models.PositiveIntegerField(default=0)),
                ('bookpath', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_liked', to='bookpaths_app.bookpath')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
