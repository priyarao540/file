from django.contrib import admin
from .models import Blog,Blog1
from .models import blogger,comapnyone,company1blogger,Registration,Temp,practiceblog,dataserializer

from .models import empblog,comblog,university,student,child,parent,subjects,teacher, StudentMany,departments

admin.site.register([Blog,Blog1,company1blogger,Temp,practiceblog,dataserializer])
admin.site.register([blogger,comapnyone,departments,Registration])
admin.site.register([empblog,subjects,teacher,StudentMany])
admin.site.register([comblog,university,student,child,parent])


# Register your models here.
