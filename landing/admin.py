from django.contrib import admin
from .models import send_data,dynamic_data

# Register your models here.

class send_(admin.ModelAdmin):
    list_display = ['FullName','Email','PhoneNumber','Name']

class admin_(admin.ModelAdmin):
    list_display = ["about","howtowork","title","banner", "Adress","admin"]


admin.site.register(send_data,send_)
admin.site.register(dynamic_data,admin_)