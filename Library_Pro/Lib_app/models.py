from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import os
from .utils import *
import uuid
from django.conf import settings
from django.db.models import Sum
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.http import JsonResponse

from importlib import import_module

from datetime import datetime
from .utils import id_generator_6
from datetime import datetime, timedelta

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

uuid.uuid4().hex[:6].upper()



class Book_Data(models.Model):
    book_id                = models.CharField(max_length=10, unique=True, null=True, blank=True)
    title                   = models.CharField(max_length=1000)
    author                   = models.CharField(max_length=1000)
    publisher                   = models.CharField(max_length=1000)
    edition                     = models.DecimalField(max_digits=20, decimal_places=2, default=18.00) 
    # book_img                     = models.DecimalField(max_digits=20, decimal_places=2, default=18.00) 
    book_img               = ProcessedImageField(upload_to='book_images/',format='png',options={'quality': 100}, null=True, blank=True)
   
    created_on                  = models.DateTimeField(auto_now_add=True)
    updated_on                  = models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        super(Book_Data,self).save()
        if not self.book_id:
            self.book_id = id_generator_6()
            self.save()
            
        
    def __str__(self):
        return str(self.id) + " " +  str(self.title)

    class Meta: 
        ordering = ['-created_on']

