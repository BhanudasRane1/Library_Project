from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import  *


# admin.site.site_header = " Last Working Day "
# admin.site.site_title = "  Last Working Day  "


# admin.site.unregister(User)
admin.site.register(Book_Data)