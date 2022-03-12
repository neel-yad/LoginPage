from asyncio.windows_events import NULL
import email
import imp
import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import users


def loginPage(request):
   if request.method=="POST":
      email=request.POST.get('email')
      password=request.POST.get('password')
      usersList=users.objects.all()
      for user in usersList:
         if user.Email==email and user.Password==password:
            return HttpResponse('''<h1>You have logged successfully</h1>''')
      return HttpResponse('''<h1>Incorrect Username or Password</h1>''')      
   return render(request,'LoginPage.html')

def newUser(request):
   if request.method=="POST":
      email=request.POST.get('email')   
      usersList=users.objects.all()
      fname=request.POST.get('fname','')   
      lname=request.POST.get('lname','')   
      password=request.POST.get('password')   
      phone_no=request.POST.get('phone_no')
      if fname=="" or lname=="":
         return HttpResponse("Please enter valid Name")
      if email=="" or password=="":
         return HttpResponse("Please enter valid email and password")
      if phone_no=="":
         return HttpResponse("Please enter valid Phone No.")
      for user in usersList:
         if user.Email==email:
            return HttpResponse("Email Already Exit ...Please try with another email")
      user=users(FirstName=fname,LastName=lname,Email=email,Password=password,PhoneNumber=phone_no)
      user.save()
      return HttpResponse('''<h1>Data Saved to Database</h1>''')
   return render(request,'users.html')   