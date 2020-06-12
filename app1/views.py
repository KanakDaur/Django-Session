from django.shortcuts import render
from app1.forms import name_form,age_form,email_form

# Create your views here.

def name_view(request):
    name_f = name_form()
    return render(request,'app1/name.html',{'name_f':name_f})

def age_view(request):
    name = request.GET['name']              # getting session value
    request.session['name'] = name          # setting session value
    age_f = age_form()
    return render(request,'app1/age.html',{'age_f':age_f})

def email_view(request):
    age = request.GET['age']
    request.session['age'] = age
    email_f = email_form()
    return render(request,'app1/email.html',{'email_f':email_f})

def all_info(request):
    email = request.GET['email']
    request.session['email'] = email
    return render(request,'app1/info.html')
