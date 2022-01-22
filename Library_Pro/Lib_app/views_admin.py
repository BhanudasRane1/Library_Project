
from django.shortcuts import render, redirect
from django.views.generic import View 
from .models import *
# from product.models import *
# from user.forms import * 
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
# from django.forms.models import model_to_dict
# from django.db.models import Q
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
# from django.views.generic import ListView, CreateView, UpdateView
# from django.urls import reverse_lazy
from .forms import *



class Book_Data_View(View):
    def get(self,request):
        template = 'admin_data/admin/admin_dashboard.html'
    #   u = self.request.user
    #   try:
        #    if u.is_staff:     
    
        try:
            book_data = Book_Data.objects.all()
            paginator = Paginator(book_data,20)
            page =  request.GET.get('page')
            book_data = paginator.get_page(page)
            print(book_data)
        except:
            book_data = None
            print("BOOOOO",book_data)

        book_data_form = Book_Data_Form()
            
        context = { 
              'book_data':book_data,                              
                #   'tax_master':tax_master,
                    'book_data_form':book_data_form,
                    # 'employer' :employer,
                } 
        return render(request, template, context)
        #   except:
        #        return redirect('unauthorized_access_url')

    def post(self,request):
        template = 'admin_data/admin/admin_dashboard.html'
        # u = self.request.user
        # try: 
        #     if u.is_staff:         
        book_data_form = Book_Data_Form(request.POST)
        
        if book_data_form.is_valid():
            print("Hello Address")
            book_data_form.save()
            messages.success(request, "Book Record Updated Successfully!")
            return redirect('book_data_url') 
        else:
            messages.warning(request, "Something went Wrong!")
        return redirect('book_data_url') 
        # except:
        #     return redirect('unauthorized_access_url')
            



@login_required
def edit_book_data(request):
    #  u = request.user
    #  if u.is_staff:
    if request.method == 'POST':
        objid = request.POST['editid']
    post = get_object_or_404(Book_Data, id=objid)
    book_data_form = Book_Data_Form(request.POST, request.FILES or None,  instance=post )
    print(objid)
    if book_data_form.is_valid():
        post = book_data_form.save(commit=False)
        post.save()
        messages.success(request, "Book Details Updated Successfully!")
        return redirect('book_data_url' )
    else:
        messages.warning(request, "Something went Wrong!")
        return redirect('book_data_url' ) 
    #  else:
    #       return redirect('tax_master_url')


@login_required
def delete_book_data(request):
    #  u = request.user
    #  if u.is_staff:
    if request.method == 'POST':
        objid = request.POST['deleteid']
    post = Book_Data.objects.get(id=objid)
    # title = post.title
    post.delete()  
    messages.success(request, "Book Record Deleted Successfully") 
    return redirect('book_data_url')
    #  else:
    #       messages.warning(request, " Something went Wrong! ") 
    #       return redirect('tax_master_url')