from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 
urlpatterns = [
   

   #Take Three Classes Logout, Login and Logout as per problem statement.
    path('logout',logout,name='logout_url'),
 
    path('login/', Login_View.as_view(), name='login_url'),
    path('signup/', Signup_View.as_view(), name='signup_url'),


    


]