# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def save(self, *args, **kwargs):
    #     try:
    #         self.validate_unique(exclude=("email_address"))
    #     except ValidationError as e:
    #         for m in e.messages():
    #             print m
    #         return
    #     super(User, self).save(*args, **kwargs)