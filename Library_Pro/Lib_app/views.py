from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View 
from .models import *
# from product.models import *
# from user.forms import * 
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import *

from django.core.mail import send_mass_mail
from django.core.mail import BadHeaderError, send_mail

from django.shortcuts import render

from django.views.generic import ListView, DetailView


# Create your views here.


def index(request):
    template = 'user_panel/index.html'
    try:
        book_data = Book_Data.objects.all()[:12]
    except:
        book_data = None
    book_data_form = Book_Data_Form()    
    context = { 
                'book_data':book_data,
                'book_data_form':book_data_form,
                
                } 
    return render(request, template, context)
