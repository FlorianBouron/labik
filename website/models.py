from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Comment(models.Model):
    book = models.ForeignKey('Book')
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + ' by ' + self.author


class Book(models.Model):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    reading_time = models.PositiveSmallIntegerField()
    cover = models.FileField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + ' by ' + self.author


class Page(models.Model):
    book = models.ForeignKey('Book')
    pageNumber = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title + ' from ' + self.book


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
