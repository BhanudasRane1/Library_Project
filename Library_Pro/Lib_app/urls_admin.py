from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views_admin import *

urlpatterns = [

    # path('', Index.as_view(), name="index_url"),
    
    path('book_data', login_required(Book_Data_View.as_view()), name="book_data_url"), 
    # path('employer_data/credit_order/<employer_id>/', login_required(Employer_Order_Detail_View.as_view()), name="credit_order_url"), 
    path('book_data/edit_book_data/', edit_book_data , name='edit_book_data_url'),
    path('book_data/delete_book_data/', delete_book_data, name='delete_book_data_url'),
    
  
    

 
]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)