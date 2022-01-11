from django.db import models
from django.contrib.auth.models import User
##whenever you do any changes in model form then it is must to do make migratimanage.pyon##
class Blog(models.Model):
    name = models.CharField(max_length=50, null=True)
    description  = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

class Blog1(models.Model):
    name = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=8,null=True)
    created_at = models.DateTimeField(auto_now=True)

class blogger(models.Model):
    name = models.CharField(max_length=50, null=True)
    middlename = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    reenterpassword = models.CharField(max_length=50, null=True)
    DOB = models.CharField(max_length=10,null=True)
    created_at = models.DateTimeField(auto_now=True)

class company1blogger(models.Model):
    name = models.CharField(max_length=50, null=True)
    middlename = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    reenterpassword = models.CharField(max_length=50, null=True)

class empblog(models.Model):
    emp_name=models.CharField(max_length=20,null=True)
    emp_des=models.CharField(max_length=30,null=True)
    blogs = models.ManyToManyField('comblog', related_name="blogs", blank=True)
    ##one (empblog) to many (comblog)relation##

class dataserializer(models.Model):
    emp_name=models.CharField(max_length=20,null=True)
    emp_des=models.CharField(max_length=30,null=True)

class comblog(models.Model):
   name = models.CharField(max_length=25,null=True)
   middle_name = models.CharField(max_length=25,null=True)
   last_name = models.CharField(max_length=25,null=True)
   password= models.CharField(max_length=8,null=True)
   reenterpassword= models.CharField(max_length=8,null=True)
   employee = models.ForeignKey(empblog, on_delete=models.SET_NULL, null=True)
   ##single relation attachement##



class student(models.Model):
    name = models.CharField(max_length=25, null=True)
    roll_no = models.CharField(max_length=25, null=True)

class university(models.Model):
    stu=models.ForeignKey(student, null=True, on_delete=models.SET_NULL)
    universityname=models.CharField(max_length=25, null=True)

class child(models.Model):
    name = models.CharField(max_length=25, null=True)
    surname = models.CharField(max_length=25, null=True)

class parent(models.Model):
    kid=models.ForeignKey(child, null=True, on_delete=models.SET_NULL)
    parentname=models.CharField(max_length=25, null=True)


class subjects(models.Model):
    subname = models.CharField(max_length=25, null=True)
    lecture = models.CharField(max_length=25, null=True)


class teacher(models.Model):
    sub = models.ForeignKey('subjects', null=True, on_delete=models.SET_NULL)
    teachername = models.CharField(max_length=25, null=True)
    #student=models.ManyToManyField("StudentMany", related_name="student_data", blank=True)


class StudentMany(models.Model):
    studentsname = models.CharField(max_length=25, null=True)

class comapnyone(models.Model):
    companyname = models.CharField(max_length=25, null=True)
    departmentinfo = models.ManyToManyField("departments", related_name="department_data", blank=True)

class departments(models.Model):

    departments_head=models.CharField(max_length=25, null=True)


class Registration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    phone_number = models.BigIntegerField(null=True)

class Registration_practice(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)




class Temp(models.Model):
    name = models.IntegerField(null=True)
    is_delete=models.BooleanField(default=False)

class practiceblog(models.Model):
    name=models.CharField(max_length=25, null=True)
    middlename=models.CharField(max_length=25, null=True)
    lastname=models.CharField(max_length=25, null=True)

class CRUDData(models.Model):
    first_name = models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True)