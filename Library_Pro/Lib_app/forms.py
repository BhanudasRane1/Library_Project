from django import forms
from django.contrib.auth.models import User
from .models import *
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import os


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class Book_Data_Form(forms.ModelForm):
    class Meta:
        model = Book_Data
        fields = ['title', 'author', 'publisher','edition','book_img']
