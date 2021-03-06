# Generated by Django 3.1.7 on 2021-04-05 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookpaths_app', '0003_book_bookpath_bookpathfollow'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPathStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookpaths_app.book')),
                ('bookpath', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookpaths_app.bookpath')),
            ],
        ),
    ]
