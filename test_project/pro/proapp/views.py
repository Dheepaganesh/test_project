from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import jwt
from proapp.models import *
from django.http import JsonResponse


def home(request):
    return render(request,'home.html')

def register(request):
    name=request.POST.get('name')
    mail=request.POST.get('mail')
    print(mail)
    passw=request.POST.get('password')
    if User.objects.filter(email=mail).exists():
        data={
            'mail':'fail',
        }
        return JsonResponse(data)
    else:   
        newusr=get_user_model()
        obj=newusr.objects.create_superuser(username=name,email=mail,password=passw)
        obj.save()
        obj1=Customer(name=name,email=mail,password=passw)
        obj1.save()
        data={
            'mail':'pass',
        }
        return JsonResponse(data)

def logincheck(request):
    try:
        mail=request.POST.get('mail')
        passw=request.POST.get('password')
        print(mail)
        obj=User.objects.get(email=mail)
        name=obj.username
        print(name)
        user=authenticate(request,username=name,email=mail,password=passw)
        print(user)
        if user is not None:
            payload = {'email': mail}
            jwt_token = jwt.encode(payload, 'secret_key', algorithm='HS256')
            return JsonResponse({'token': jwt_token})
        else:
            return JsonResponse({'token':0})
    except:
        return JsonResponse({'token':0})

def welcome(request):
    token=request.GET.get('token')
    return render(request,'main.html')

def aboutpage(request):
    return render(request,'about.html')