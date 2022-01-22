from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Lib_app.views import *

urlpatterns = [

    # path('', Index.as_view(), name="index_url"),
    # path('resume_signup/', Resume_Data.as_view(), name='resume_url'),
    # path('cand_register/', Cand_Register.as_view(), name='cand_register_url'),
    
    # path('cand_register/cpy/', Cand_Register_cpy.as_view(), name='cand_register_cpy_url'),
    
    path('', index, name="index_url"),

    # path('accounts/google/login/', google_signup, name="google_signup_url"),

    # path('all_jobs/', Job_View.as_view(), name="job_url"),

    # path('job_description/<id>/', Job_Description_View.as_view(), name="job_description_url"),


    # path('about', about, name="about_url"),
    # # path('register', register, name="register_url"),
    # path('contact/', Contact_Data.as_view(), name='contact_url'),
    # path('product/', Product_Purchase_View.as_view(), name='product'),

    # path('register/', Register_User.as_view(), name='register_url'),

    
    # path('blog/', Blog.as_view(), name='blog_url'),

    # path('blog_post/blog_detail/<id>', Blog_Detail_View.as_view(), name="blog_detail_user_url"), 
    

    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    # # path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    # path('add-to-cart/<product_id>/', add_to_cart, name='add-to-cart'),
    # # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    # path('remove-from-cart/<product_id>/', remove_from_cart, name='remove-from-cart'),
    # path('remove-product-from-cart/<product_id>/', remove_single_product_from_cart, name='remove-single-product-from-cart'),

    # # path('accomodation/', accomodation, name="accomodation_url"),
    # # path('contact/', contact, name="contact_url"),


    # path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),

]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)