# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
import datetime
from django.db import models
from .youtubeAPI import youtube_search
# Create your models here


def get_expiration_date():
    data = datetime.datetime.now() + datetime.timedelta(days=5)
    return data


class UserInformation(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, unique=True)
    coin = models.IntegerField()


class Drink(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)


class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    drinks = models.ManyToManyField(Drink, related_name="cocktails")
    prix = models.IntegerField(default=5)

    def save(self, *args, **kwargs):
        super(Cocktail, self).save(*args, **kwargs)
        link = youtube_search(self.name)

        Video.objects.create(url=link, cocktail=self)

    def enoughmoney(self , user):
        if user is None:
            return False
        if user.userinformation.coin < self.prix:
            return False
        else:
            return True


class Video(models.Model):
    url = models.CharField(max_length=100)
    cocktail = models.OneToOneField(Cocktail, on_delete=models.CASCADE, unique=True)


class Queue(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, default=1)


class Token(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, unique=True)
    hash = models.CharField(max_length=100)
    expiration_date = models.DateTimeField(default=get_expiration_date)

    def is_expired(self):
        return self.expiration_date < timezone.now()


