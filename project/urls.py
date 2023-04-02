from django.contrib import admin
from django.urls import path
from project import views

urlpatterns = [
    path("",views.index,name="index"),
    path("avm/about",views.about,name='about'),
    path("avm/services",views.services,name='services'),
    path("avm/services1",views.services1,name='services1'),
    path("avm/contact",views.contact,name='contact'),
    path("avm/featured",views.featured,name='featured'),
    # path("avm/login",views.loginUser,name='login'),
    # path("avm/register",views.register,name='register'),
    # path("avm/logout",views.logoutUser,name='logout'),
    # path("avm/customer",views.customer,name='customer')
    # path("loop",views.loop,name='loops')
    path('avm/register',views.signup,name='reg'),
    path('avm/login',views.loginPage,name='login'),
    path('avm/customer',views.HomePage,name='Home'),
    path('avm/logout',views.logoutUser,name='logout'),
    path("avm/customer/contact",views.contactcus,name='contact'),

    path('avm/customer/h1',views.h1,name='h1'),
    path('avm/customer/h2',views.h2,name='h2'),
    path('avm/customer/h3',views.h3,name='h3'),
    path('avm/customer/pay',views.pay,name='pay')



]
