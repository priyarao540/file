"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path
from gauranj.views import abc,pqr,xyz,home,Login,name,user,DeleteHome,practice,delpractice,editpractice,\
     practiceForm,emp,deletehome,edithome,company,deleteemplist,editemplist,EmployeModelForm,crud_data,\
    newblogform, CompanyclientForm,company1,SendEmail,email,foreignkeyonview,ForeignExample,ForeignExample2, \
    foreignExample3,ManytomanyExample,manytomanyex2,Registartion1,Login1,logout_user,home1,DeleteData,delete_dummy

from gauranj.views import *
# from satish.views import mno,stu,form,registration_from,satishLogin1,satishlogout_user


from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from gauranj.views import *
router = routers.SimpleRouter(trailing_slash=False)
router.register(r"^crud", CRUDDataSerializer, basename="user")
router.register(r"^signup", SignupViewset, basename="user")
router.register(r"^login", LoginViewset, basename="user")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',abc),
    path('home0',pri),
    path('home1',pqr),
    path('home2',xyz),
    path('home3',home),
    #path('home4',mno),
    #path('home5',stu),
    #path('Home6',form),
    re_path("class_home/(?P<id>[0-9]+)?$", Login.as_view()),
    re_path("class_home1/(?P<id>[0-9]+)?$",companylogin.as_view()),
    # re_path("satishLogin1/(?P<id>[0-9]+)?$", satishLogin1.as_view(),name='loginsatish'),
    # re_path("satishLogout1/(?P<id>[0-9]+)?$", satishlogout_user,name='satishLogout1'),
    #re_path("sign_up/(?P<id>[0-9]+)?$", registration_from.as_view()),
    re_path("name/(?P<id>[0-9]+)?$", name.as_view()),
    re_path("usrdetails/(?P<id>[0-9]+)?$", user.as_view(),name='usrdetails'),
    re_path("company1user/(?P<id>[0-9]+)?$", company1user.as_view(),name='company1user'),

    re_path("delete_details/(?P<id>[0-9]+)?$", DeleteHome.as_view(),name='delete_details'),
    re_path("employee_details/(?P<id>[0-9]+)?$", emp.as_view(),name='employee_details'),
    re_path("employee_del_details/(?P<id>[0-9]+)?$",deletehome.as_view(),name='employee_del_details'),

    re_path("employee_edit_details/(?P<id>[0-9]+)?$",edithome.as_view(),name='employee_edit_details'),
    re_path("company/(?P<id>[0-9]+)?$",company.as_view()),
    re_path("comdetails/(?P<id>[0-9]+)?$",company1.as_view(),name='comdetails'),

    re_path("deldetails/(?P<id>[0-9]+)?$",deleteemplist.as_view(),name='deldetails'),
    re_path("editdetails/(?P<id>[0-9]+)?$",editemplist.as_view(),name='editdetails'),

    re_path("formredirect/(?P<id>[0-9]+)?$",EmployeModelForm.as_view(),name='formredirect'),
    re_path("formredirect2/(?P<id>[0-9]+)?$",newblogform.as_view(),name='formredirect2'),
    re_path("formredirect1/(?P<id>[0-9]+)?$",CompanyclientForm.as_view(),name='formredirect1'),
    re_path("sendemail/(?P<id>[0-9]+)?$",SendEmail.as_view(),name='sendemail'),
    re_path("sendemail1/(?P<id>[0-9]+)?$",email.as_view(),name='sendemail1'),
    re_path("foreignkey1/(?P<id>[0-9]+)?$",foreignkeyonview.as_view(),name='foreignkey1'),
    re_path("foreignkey2/(?P<id>[0-9]+)?$",ForeignExample.as_view(),name='foreignkey2'),
    re_path("foreignkey3/(?P<id>[0-9]+)?$",ForeignExample2.as_view(),name='foreignkey3'),
    re_path("fkey/(?P<id>[0-9]+)?$",foreignExample3.as_view(),name='fkey'),
    re_path("mkey/(?P<id>[0-9]+)?$",ManytomanyExample.as_view(),name='mkey'),
    re_path("mkey1/(?P<id>[0-9]+)?$",manytomanyex2.as_view(),name='mkey1'),
    re_path("reg1/(?P<id>[0-9]+)?$",Registartion1.as_view(),name='reg'),
    re_path("log1/(?P<id>[0-9]+)?$",Login1.as_view(),name='log1'),
    re_path("log2/(?P<id>[0-9]+)?$",logout_user,name='logout'),
    re_path("priyalog/(?P<id>[0-9]+)?$",home1,name='homelogout'),
    path("delete_data/", DeleteData.as_view(), name="delete_data"),
    path("delete_dummy/<int:id>",delete_dummy,name="delete_dummy"),
    #path("delete_data1/", Deletedata2.as_view(), name="delete_data1"),
    #path("delete_dummy1/<int:id>", delete_dummy1, name="delete_dummy1"),
    re_path("practicee/(?P<id>[0-9]+)?$", practice.as_view(), name='practicee12'),
    re_path("practice_form/(?P<id>[0-9]+)?$", practiceForm.as_view(), name='practice_form'),
    re_path("del_pra/(?P<id>[0-9]+)?$", delpractice.as_view(), name='del_pra'),
    re_path("edit_pra/(?P<id>[0-9]+)?$", editpractice.as_view(), name='edit_pra'),
    re_path("praemail/(?P<id>[0-9]+)?$",  practice_email.as_view(), name='praemail'),
    re_path("praereg/(?P<id>[0-9]+)?$",  practice_regi.as_view(), name='pracrego'),
    re_path("pralog/(?P<id>[0-9]+)?$",  practice_Login.as_view(), name='pralog'),
    re_path("class_data/(?P<id>[0-9]+)?$", APIData.as_view(), name='class_data'),
    path("crud_data/", crud_data, name="crud_data"),
    path("crud_data1/<int:id>", crud_data_update, name="crud_data1"),

]
urlpatterns += format_suffix_patterns(router.urls)
