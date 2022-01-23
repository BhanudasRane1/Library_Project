
from django.shortcuts import render, redirect
from django.views.generic import View 
from .models import *

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth.decorators import login_required

from .forms import *


# We are use class based view for get and post method 
# For edit and Delete We use function based view.


# Class Start Contain Get And Post 
class Book_Data_View(View):
    def get(self,request):
        template = 'admin_data/admin/admin_dashboard.html'
        try:
            try:
                # For Paginator
                book_data = Book_Data.objects.all()
                paginator = Paginator(book_data,20)
                page =  request.GET.get('page')
                book_data = paginator.get_page(page)
            except:
                book_data = None
              

            book_data_form = Book_Data_Form()
                
            context = { 
                'book_data':book_data,                              
                  'book_data_form':book_data_form,
                        
                    } 
            return render(request, template, context)
        except:
            return redirect('unauthorized_access_url')

    def post(self,request):
        template = 'admin_data/admin/admin_dashboard.html'
        try: 
            book_data_form = Book_Data_Form(request.POST)
            
            if book_data_form.is_valid():
                print("Hello Address")
                book_data_form.save()
                messages.success(request, "Book Record Updated Successfully!")
                return redirect('book_data_url') 
            else:
                messages.warning(request, "Something went Wrong!")
            return redirect('book_data_url') 
        except:
            return redirect('unauthorized_access_url')
            

# Class End ...



#Function For Edit start.........
@login_required
def edit_book_data(request):
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
   

#Function For Edit End........

#Function For Delete start.........
@login_required
def delete_book_data(request):
    if request.method == 'POST':
        objid = request.POST['deleteid']
    post = Book_Data.objects.get(id=objid)
   
    post.delete()  
    messages.success(request, "Book Record Deleted Successfully") 
    return redirect('book_data_url')


#Function For Delete end.........
