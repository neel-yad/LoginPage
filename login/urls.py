from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.loginPage,name="LoginPage"),
    path('newUser/',views.newUser,name="NewUser")
]
