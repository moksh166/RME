from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from project.models import Contact1
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
#mongodb serializers
# from django.views.decorators.csrf import  csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from project.models import Profile
# from project.serializers import ProfileSerializer
# Create your views here.
# def index(request):
#     b="no"
#     c="name"
#     a={
#         'fname':b,
#         'lname':c
#     }
#     return render(request,"index.html",a)
# from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def navbar(request):
    return render(request,'navbar.html')
def about(request):
    return HttpResponse("this is a about page")
def services(request):
    return render(request,"services.html")
def services1(request):
    return render(request,"services1.html")
def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('f_name')
        email=request.POST.get('f_email')
        phone=request.POST.get('f_phone')
        query=request.POST.get('f_query')
        contact=Contact1(name=name,email=email,phone=phone,query=query,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')
    return render(request,'contact.html')
def contactcus(request):
    if(request.method=="POST"):
        name=request.POST.get('f_name')
        email=request.POST.get('f_email')
        phone=request.POST.get('f_phone')
        query=request.POST.get('f_query')
        contact=Contact1(name=name,email=email,phone=phone,query=query,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')
    return render(request,'contact1.html')
def featured(request):
    return render(request,'featured.html')
# def loginUser(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         print(username,password)
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect("/avm/customer")
#         else:
#             return render(request,'login.html')
#     return render(request,'login.html')

# def register(request):
#     return render(request,'register.html')

# def logoutUser(request):
#     logout(request)
#     return render(request,'index.html')
# def customer(request):
    
#     if request.user.is_anonymous:
#         messages.warning(request,"Invalid user")
#         return redirect("/avm/login")
#     return render(request,"customer.html")
@login_required(login_url='login')
def HomePage(request):
    return render(request,'customer.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('rpassword')
        if(pass1!=pass2):
            messages.warning(request,'passwords did not match')
        
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request,'Your account has been successfully created')
            return redirect('login')
    return render(request,'register.html')
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Welcome Back')
            return redirect('Home')
        else:
            messages.warning(request,'username or password is incorrect')
        
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect('login')

# @csrf_exempt
# def ProfileApi(request,id=0):
#     if request.method=='GET':
#         profiles=Profile.objects.all()
#         profiles_serializer=ProfileSerializer(profiles,many=True)
#         return JsonResponse(profiles_serializer.data,safe=False)
    
#     elif request.Method=='POST':
#         profile_data=JSONParser().parse(request)
#         profiles_serializer=ProfileSerializer(data=profile_data)
#         if profiles_serializer.is_valid():
#             profiles_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
    
#     elif request.method=='PUT':
#         profile_data=JSONParser().parse(request)
#         profile=Profile.objects.get(ProfileId=profile_data['ProfileId'])
#         profiles_serializer=ProfileSerializer(profile,data=profile_data)
#         if profiles_serializer.is_valid():
#             profiles_serializer.save()
#             return JsonResponse("Update Successfully",safe=False)
#         return JsonResponse("Failed to update")
#     elif request.method=='DELETE':
#         profile=Profile.objects.get(ProfileId=id)
#         profile.delete()
#         return JsonResponse("Deleted successfully",safe=False)
# def add_profile(request):
#     if request.method=="POST":
#         prof=request.POST.get('f_name')
#         Profile.objects.create(prof)
# def update_profile(request,id):
#     pass
# def delete_profile(request,id):
#     pass
# def read_profile(request,id):
#     pass
# def read_all(request,id):
#     pass

def h1(request):
    return render(request,'h1.html')
def h2(request):
    return render(request,'h1.html')
def h3(request):
    return render(request,'h1.html')
def pay(request):
    return render(request,'payment.html')