"""
URL configuration for waste_food_management_and_donation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),

    path('register1/',views.register1,name='register'),
    path('login/',views.login,name='login'),
    # path('profile/',views.profile,name='profile'),
    # path('demo/',views.demo,name='demo'),
    path('restaurantss/',views.restaurantss,name='restaurant'),
    path('addfood/',views.addfood,name='food'),
    path('donatefood/',views.donatefood,name='donatefood'),
    path('newfile/',views.newfile,name='newfile'),

    # path('update/',views.update,name='update'),
    # path('updateprofile/',views.updateprofile,name='updateprofile'),

    path('restaurant_reg/',views.restaurant_reg,name='registerr'),
    path('restaurant_login/',views.restaurant_login,name='loginnn'),
    path('restaurant_profile/',views.restaurant_profile,name='resprofile'),

    # path('error_template/',views.error_template,name='tem'),
    # path('viewdonations/',views.viewdonations,name='viewdonation'),

    
    path('history/',views.history,name='history'),
    path('NGO/',views.NGO,name='NGO'),
    path('NGOREGISTER/',views.NGOREGISTER,name='NGOregister'),
    path('NGOlogin/',views.NGOlogin,name='login'),
    path('donate/',views.donate,name='Donate'),
    path('feedback/',views.feedback,name='Feedback'),
    path('sendcomplaints/',views.sendcomplaints,name='sentcomplaints'),
    path('NGOemployee/',views.NGOemployee,name='NGOemployee'),
    path('NGOemployeeRegister/',views.NGOemployeeRegister,name='NGOemployeeregister'),
    path('NGOemployeelogin/',views.NGOemployeelogin,name='NGOemployeelogin'),
    path('addrequest/',views.addrequest,name='addrequest'),
    path('view_donation/',views.view_donation,name='view_donation'),
    path('delete/<int:id>',views.delete,name='delete'),

    path('view_donationcopy/',views.view_donationcopy,name='view_donationcopy'),
    path('ngoviewrequest/',views.ngoviewrequest,name='ngoviewrequest'),
    path('viewemployee/',views.viewemployee,name='viewemployee'),



    path('Addemployeess/',views.Addemployeess,name='Addemployees'),
    

    path('ngoviewdonation/',views.ngoviewdonation,name='ngoviewdonation'),
    path('foodbooking/<int:item_id>/',views.foodbooking,name='foodbooking'),
    path('save_booking/', views.save_booking, name='save_booking'),



    path('update_status/<int:id>/', views.update_status, name='update_status'),
    path('update_status_worker/<int:id>/', views.update_status_worker, name='update_status_worker'),


    path('viewassignedworks/', views.viewassignedworks, name='viewassignedworks'),
    path('viewemployeedelete/<int:id>',views.viewemployeedelete,name='viewemployeedelete'),

    path('ngo_profile/',views.ngo_profile,name='ngo_profile'),
    path('ngoemployeprofile/',views.ngoemployeprofile,name='ngoemployeprofile'),




    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminaddfood/',views.adminaddfood,name='adminaddfood'),
    path('admincomplaints/',views.admincomplaints,name='admincomplaints'),
    path('adminfeedback/',views.adminfeedback,name='adminfeedback'),
    path('adminngoemployeeregister/',views.adminngoemployeeregister,name='adminngoemployeeregister'),
    path('adminngoregister/',views.adminngoregister,name='adminngoregister'),
    path('adminrestaurant/',views.adminrestaurant,name='adminrestaurant'),
    path('adminaddemployee/',views.adminaddemployee,name='adminaddemployee'),
    path('bookingfoods/',views.bookingfoods,name='bookingfoods'),
    path('adminregister/',views.adminregister,name='adminregister'),
    path('Addfooddelete/<int:id>',views.Addfooddelete,name='adddelete'),
    path('complaintsdelete/<int:id>',views.complaintsdelete,name='complaintsdelete'),
    path('Admin1/',views.Admin1,name='Admin1'),
    path('feedbackdelete/<int:id>',views.feedbackdelete,name='feedbackdelete'),
    path('ngoregisterdelete/<int:id>',views.ngoregisterdelete,name='ngoregisterdelete'),
    path('addemployeedelete/<int:id>',views.addemployeedelete,name='addemployeedelete'),
    path('restaurantdelete/<int:id>',views.restaurantdelete,name='restaurantdelete'),
    path('bookingfooddelete/<int:id>',views.bookingfooddelete,name='bookingfooddelete'),
    path('Adminregdelete/<int:id>',views.Adminregdelete,name='Adminregdelete'),
]


