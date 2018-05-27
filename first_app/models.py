# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Topic(models.Model):
  url_name = models.CharField(max_length=264,unique=True)
  short_url= models.CharField(max_length=6,unique=True)
