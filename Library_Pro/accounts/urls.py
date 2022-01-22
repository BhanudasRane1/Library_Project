from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 
urlpatterns = [
    # path('register',views.register,name='register'),
    # path('login',views.login,name='login'),
    path('logout',logout,name='logout_url'),
    # path('login',views.login,name='login'),
    path('login/', Login_View.as_view(), name='login_url'),
    path('signup/', Signup_View.as_view(), name='signup_url'),


    


]