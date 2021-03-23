import os

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


def get_image_path(instance, filename):
    return os.path.join('covers', str(instance.id), filename)


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f'Category: {self.name}'


class BookPath(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.CharField(max_length=240, blank=False, null=False)
    author = models.ManyToManyField(User, related_name='proposed_paths')
    category = models.ManyToManyField(Category, related_name='paths')
    follow_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Bookpath: {self.name}'


class BookPathFollow(models.Model):
    CANCELLED = -1
    NOT_STARTED = 0
    WORK_IN_PROGRESS = 1
    FINISHED = 2

    Status = (
        (CANCELLED, 'Cancelled'),
        (NOT_STARTED, 'Not started'),
        (WORK_IN_PROGRESS, 'Work in progress'),
        (FINISHED, 'Bookpath completed'),
    )

    bookpath = models.ForeignKey(
        BookPath, on_delete=models.CASCADE, related_name='is_liked')
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes')
    status = models.IntegerField(choices=Status, default=NOT_STARTED)
    current_step = models.PositiveIntegerField(default=0)


@receiver(post_save, sender=BookPathFollow)
def increase_bookpath_follows(sender, instance, created, **kwargs):
    bookpath = BookPath.objects.get(id=sender.bookpath)
    bookpath.follow_count += 1
    bookpath.save()


@receiver(pre_delete, sender=BookPathFollow)
def decrease_bookpath_follows(sender, instance, created, **kwargs):
    bookpath = BookPath.objects.get(id=sender.bookpath)
    bookpath.follow_count -= 1
    bookpath.save()


class Book(models.Model):
    isbn_10 = models.CharField(validators=[RegexValidator(
        regex='\w.{10}$', message='ISBN-10 length has to be 10')], max_length=10, primary_key=True)
    isbn_13 = models.CharField(validators=[RegexValidator(
        regex='\w.{13}$', message='ISBN-13 length has to be 13')], max_length=13, blank=False, null=False)
    title = models.CharField(max_length=240, blank=False, null=False)
    author = models.CharField(max_length=240, blank=False, null=False)
    cover = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    publishers = models.CharField(max_length=240, blank=False, null=False)
    number_of_pages = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'