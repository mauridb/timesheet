# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=256, blank=True)
    preview = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)


class Timesheet(models.Model):
    profile = models.ForeignKey(Profile, blank=False, null=False)
    project = models.CharField(max_length=256)
    month = models.CharField(max_length=50)
    day = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    launch = models.BooleanField()
    skills = models.ManyToManyField(Skill)
    task = models.TextField(max_length=256)
    team = models.TextField(max_length=256)
    notes = models.TextField(max_length=500)
