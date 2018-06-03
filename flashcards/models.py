# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Deck(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=256, null=False, blank=True)