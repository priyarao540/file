from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import *
from .forms import EmployeeForm,ClientForm,blogform,blogformpractice
from  Blog.settings import EMAIL_HOST_USER as my_email
from django.core.mail import send_mail
from django.contrib.auth import authenticate, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token



def abc(request):
    return HttpResponse("Hi all")
def pri(request):
    return HttpResponse("chao")

def pqr(request):
    return HttpResponse("hi all!!!!!")

def xyz(request):
    return HttpResponse("doing great")

def home(request):
    return render(request,"home.html")

class Login(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

class companylogin(View):
    def get(self,request,*args,**kwargs):
        return render(request,'companylogin1.html')

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        Blog1.objects.create(name=data("username"),password=data("password"))
        return render(request,'companylogin1.html')


class name(View):
    def get(self, request, *args, **kwargs):
        return render(request,'demo_regi.html')

    def post(self, request, *args, **kwargs):
        data = self.request.POST.get
        Blog.objects.create(name=data("blogname"),description=data("blogdesc"))
        return render(request,'demo_regi.html')
###############
class user(View):
    def get(self,request,*args,**kwargs):
        blog_data=blogger.objects.all()
        return render(request,'registration_from.html',{'data':blog_data})

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        print(data)
        blogger.objects.create(name=data("name"),middlename=data("middlename"),lastname=data("lastname"),password=data("password"),
        reenterpassword=data("reenterpassword"),DOB=data("dateofbirth"))
        ##eturn redirect("usrdetails")
        return JsonResponse(data={"message": "Blog created successfully", "status": 1}) ##use of ajex to create blog&##
        ##jasonresponse use to read or get data#


class company1user(View):
   def get(self,request,*args,**kwargs):
        data1=company1blogger.objects.all()
        return render(request,'company registrationform 1.html',({'data':data1}))

   def post(self,request,*args,**kwargs):
       data=self.request.POST.get
       print(data)
       company1blogger.objects.create(name=data("name"),middlename=data("middlename"),password=data("password"),reenterpassword=data("reenterpassword"))
       # return redirect("company1user")
       return JsonResponse(data={"message": "Blog created successfully", "status": 1})

class DeleteHome(View):

    def get(self, request, *args, **kwargs):
        print(kwargs)
        queryset = blogger.objects.get(id=kwargs["id"]).delete()
        print("querset==>",queryset)
        return JsonResponse(data={"message": "Blog deleted successfully", "status": 1})##use of ajex to delete blog&##
        ##jasonresponse use to read or get data###


# home work

class emp(View):

    def get(self,request,*args,**kwargs):
        blog_empdata=empblog.objects.all()
        return render(request,'employee.html',{'emp_data':blog_empdata})

    def post(self,request,*args,**kwargs):
        emp_data=self.request.POST.get
        print(emp_data)
        empblog.objects.create(emp_name=emp_data("name"), emp_des=emp_data("des"))
        return JsonResponse(data={"message": "Blog created successfully", "status": 1})
           ## return redirect("employee_details")


class deletehome(View):

    def get(self,request, *args, **kwargs):
        print(kwargs)
        queryset1= empblog.objects.get(id=kwargs["id"]).delete()
        print("querset2==>", queryset1)
        return JsonResponse(data={"message": "Employee deleted successfully", "status": 1})



class edithome(View):

    def get(self,request,*args,**kwargs):
        print(kwargs)
        queryset1=empblog.objects.get(id=kwargs["id"])
        return render(request,'edit.html',{'emp_data':queryset1})

    def post(self,request,*args,**kwargs):
        emp_data=self.request.POST.get
        print(emp_data)
        empblog.objects.filter(id=kwargs["id"]).update(emp_name=emp_data("name"),emp_des=emp_data("desc"))
        return  JsonResponse(data={"message": "Blog edited successfully", "status": 1})


class EmployeModelForm(View):
#shortcut to use create query
#how to create template using form without html coding,use of bootstrap.
    def get(self, *args, **kwargs):
        form = EmployeeForm()
        return render(self.request, "form2.html", {"form": form})

    def post(self, *args, **kwargs):
        form = EmployeeForm(self.request.POST)
        if form.is_valid():
            form.save()#shortcut to use create query
        return redirect("formredirect")

class company(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        return render(request,'company_registration_form.html')


    def post(self,*args,**kwargs):
        data=self.request.POST.get
        blog=comblog.objects.create(name=data("name"),middle_name=data("middlename"))
        return JsonResponse(data={"message": "Blog created successfully", "status": 1})
        #return redirect("comdetails")
        #return render(request,'company_registration_form.html')


class company1(View):# create query#
    def get(self,request,*args,**kwargs):
        print(kwargs)
        data_company=comblog.objects.all()
        return render(request,'company_registration_form.html',{'data':data_company})

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        print(data)
        comblog.objects.create(name=data("name"),middle_name=data("middle_name"),last_name=data("lastname")
                               ,password=data("password"),reenterpassword=data("repassword"))
        return JsonResponse(data={"message": "Blog created successfully", "status": 1})
    ## use of jsonresponse is onle while using ajex ##

# delete query#
class deleteemplist(View):
    def get(self,*args,**kwargs):
        print(kwargs)
        findquery=comblog.objects.get(id=kwargs["id"]).delete()
         ##return redirect("comdetails")
        return JsonResponse(data={"message": "Blog deleted successfully", "status": 1})


 #update or edit query
class editemplist(View):

    def get(self,request,*args,**kwargs):
        print(kwargs)
        findquery=comblog.objects.get(id=kwargs["id"])
        return render(request,'edit2.html',{'emp_data':findquery})


    def post(self,request,*args,**kwargs):
        emp_data=self.request.POST.get
        print(emp_data)
        comblog.objects.filter(id=kwargs["id"]).update(name=emp_data("name"),middle_name=emp_data("desc"),last_name=emp_data("last_name"),password=emp_data("password"),reenterpassword=emp_data("reenterpassword"))
        #return redirect("comdetails")

        return JsonResponse(data={"message": "Blog edited successfully", "status": 1})

class CompanyclientForm(View):   ##crate table usinf form with use of models name (pick models field automatically)##

    def get(self, *args, **kwargs):
        form = ClientForm()
        return render(self.request, "form3.html", {"form": form})

    def post(self, *args, **kwargs):
        form = ClientForm(self.request.POST)
        if form.is_valid():
            form.save()#shortcut to use create queryh
        return redirect("formredirect1")

class newblogform(View):
    def get(self,*args,**kwargs):
        form=blogform
        return render(self.request,"form3.html",{"form":form})

    def post(self,*args,**kwargs):
        form=blogform(self.request.POST)
        if form.is_valid():
            form.save()
        return redirect("formredirect2")


## send email##

class SendEmail(View):

    def get(self, *args, **kwargs):
        return  render(self.request, 'email.html')

    def post(self, *args, **kwargs):
        data = self.request.POST.get
        res = send_mail(data("subject"), data("emailbody"), my_email, [data("email")])
        return HttpResponse("<h1>email sent successfully</h1>")

class email(View):
    def get(self,*args,**kwargs):
        return render(self.request, 'email1.html')

    def post(self,*args,**kwargs):
          data=self.request.POST.get
          res = send_mail(data("subject"),data("bodytext"),my_email,[data("email")])
          return HttpResponse("<h1> your email has been sent</h1>")

class foreignkeyonview(View):
    def get(self,request,*args,**kwargs):
       return render(request,'_foreign.html')

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        empblog1=empblog.objects.get(id=data("foreignkey"))
        print(empblog)
        print(data)
        comblog.objects.create(name=data("name"),middle_name=data("middlename"),last_name=data("lastname"),password=data("password"),
        reenterpassword=data("reenterpassword"),employee=empblog1)
        return redirect("foreignkey1")

class ForeignExample(View):
    def get(self,request,*args,**kwargs):
       return render(request,'student.html')

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        stus= student.objects.create(name=data("name"),roll_no=data("rollno"))
        uni= university.objects.create(universityname=data("uniname"),stu=stus)
        return redirect("foreignkey2")

class ForeignExample2(View):
    def get(self,request,*args,**kwargs):
       return render(request,'foreignkeyex2.html')

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        chi= child.objects.create(name=data("kidname"),surname=data("kid_s_name"))
        par= parent.objects.create(parentname=data("pname"),kid=chi)
        return redirect("foreignkey3")

class foreignExample3(View):
    def get(self,request,*args,**kwargs):
       return render(request,'foreignex.html')

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        subj= subjects.objects.create(subname=data("subname"),lecture=data("lec"))
        #subj= subjects.objects.get(id=1)
        teach= teacher.objects.create(teachername=data("tname"),sub=subj)
        return redirect("fkey")



class ManytomanyExample(View):
    def get(self,request,*args,**kwargs):
       return render(request,'manytomanyex.html')

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        stu=StudentMany.objects.get(id=data("sname"))
        teach= teacher.objects.create(teachername=data("tname"))
        teach.student.add(stu)
        return redirect("mkey")

class manytomanyex2(View):
    def get(self,request,*args,**kwargs):
        return render(request,'manytomanyex3.html')

    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        dep=departments.objects.get(id=data("dh"))
        print(dep)
        com=comapnyone.objects.create(companyname=data("comname"))
        com.departmentinfo.add(dep)
        return redirect("mkey1")

class Registartion1(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, "registerform.html")

    def post(self, request, *args, **kwargs):
        data = request.POST.get
        ##create_user only supports user##
        user = User.objects.create_user(username=data("username"), email=data("email"), password=data("password"))
        Registration.objects.create(user=user, age=data("age"), phone_number=data("phone_number"))
        #return HttpResponse("Registation completed successfully")
        return redirect("log1")


class Login1(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'loginme.html')

    def post(self, request, *args, **kwargs):
        data = request.POST.get
        print(data)
        user = authenticate(username=data("username"), password=data("password"))
        if user is not None:
            return redirect("homelogout")
        else:
            return HttpResponse("soemthing went wrong")

def logout_user(request):
    logout(request)
    return redirect("log1")

def home1(request):
    return render( request,"logmeout.html",{"user":request.user.username})


class DeleteData(View):

    def get(self, *args, **kwargs):
        data = Temp.objects.filter(is_delete=False)
        return render(self.request, 'hard\hsdelete.html', {"data": data})


def delete_dummy(request, id):
    Temp.objects.filter(id=id).update(is_delete=True)
    return redirect("delete_data")


class practice(View):

    def get(self,request,*args,**kwargs):
        blogdata=practiceblog.objects.all()
        #blogdata1 = practiceblog.objects.get(id=kwargs["id"]).delete()
        return render(request,'practice1.html',{'data':blogdata})


    def post(self,request,*args,**kwargs):
        data=self.request.POST.get
        practiceblog.objects.create(name=data("myname"),middlename=data("mymiddlename"),lastname=data("mylastname"))
        return JsonResponse(data={"message": "Blog created successfully", "status": 1})
        # return redirect("practicee12")


class delpractice(View):
    def get(self,request,*args,**kwargs):
        data=practiceblog.objects.get(id=kwargs["id"]).delete()
        #return redirect("practicee12")
        return JsonResponse(data={"message": "Blog deleted successfully", "status": 1})
class editpractice(View):
    def get(self,request,*args,**kwargs):
        mydata=practiceblog.objects.get(id=kwargs["id"])
        return render(request,'practiceedit.html',{'data':mydata})

    def post(self,request,*args,**kwargs):
         data=self.request.POST.get
         practiceblog.objects.filter(id=kwargs["id"]).update(name=data("name1"),middlename=data("namemiddle"),lastname=data("namelast"))
         return JsonResponse(data={"message": "Blog edited successfully", "status": 1})

         #return redirect('practicee12')

class practiceForm(View):
#shortcut to use create query
#how to create template using form without html coding,use of bootstrap.
    def get(self, *args, **kwargs):
        form = blogformpractice()
        return render(self.request, "form2.html", {"form": form})

    def post(self, *args, **kwargs):
        form = blogformpractice(self.request.POST)
        if form.is_valid():
            form.save()#shortcut to use create query
        return redirect("formredirect")

class practice_email(View):
    def get(self,*args,**kwargs):
        return render(self.request, 'email1.html')

    def post(self,*args,**kwargs):
          data=self.request.POST.get
          res = send_mail(data("subject"),data("bodytext"),my_email,[data("email")])
          return HttpResponse("<h1> your email has been sent</h1>")

class practice_regi(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, "register_form.html")

    def post(self, request, *args, **kwargs):
        data = request.POST.get
        ##create_user only supports user##
        user = User.objects.create_user(username=data("username"), email=data("email"), password=data("password"))
        #Registration.objects.create(user=user1, age=data("age"), dateofbirth=data("dob"))
        #return HttpResponse("Registation completed successfully")
        return redirect("pracrego")

class practice_Login(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'loginme.html')

    def post(self, request, *args, **kwargs):
        data = request.POST.get
        print(data)
        user = authenticate(username=data("username"), password=data("password"))
        if user is not None:
            return redirect("homelogout")
        else:
            return HttpResponse("soemthing went wrong")

def logout_user(request):
    logout(request)
    return redirect("pracrego")

def home1(request):
    return render( request,"logmeout.html",{"user":request.user.username})



@api_view(['GET','POST'])
def crud_data(request):
    if request.method == "GET":
        crud= Blog.objects.all()
        print(crud)
        serializer=CRUDdataserializer(crud, many=True)
        response = {
            "status": "success",
            "message": "CRUDDATA list",
            "data": serializer.data,
            "status_code": 200,
        }
        return Response(response)
    elif request.method == "POST":
        serializer = CRUDdataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "CRUDDATA created successfully",
                "data": serializer.data,
                "status_code": 200,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'PUT'])  #by function#
def crud_data_update(request, id):
    queryset = Blog.objects.get(id=id)
    if request.method == "DELETE":
            queryset.delete()
            response = {
                "status": "success",
                "message": "CRUDDATA deleted successfully",
                "data": [],
                "status_code": 204,
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = CRUDdataserializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "CRUDDATA updated successfully",
                "data": serializer.data,
                "status_code": 200,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class APIData(APIView): #by class#

    def get(self, request, format=None):
        crud = Blog.objects.all()
        serializer = CRUDdataserializer(crud, many=True)
        response = {
            "status": "success",
            "message": "CRUDDATA list",
            "data": serializer.data,
            "status_code": 200,
        }
        return Response(response)

    def post(self, request, id=None, format=None):
        serializer = CRUDdataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "CRUDDATA created successfully",
                "data": serializer.data,
                "status_code": 200,
            }
            return Response(response, status=status.HTTP_201_CREATED)


    def put(self, request, id, format=None):
        queryset = Blog.objects.get(id=id)
        serializer = CRUDdataserializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "message": "CRUDDATA updated successfully",
                "data": serializer.data,
                "status_code": 200,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        queryset = Blog.objects.get(id=id)
        queryset.delete()
        response = {
            "status": "success",
            "message": "CRUDDATA deleted successfully",
            "data": [],
            "status_code": 204,
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

##below three lines of code work for crud in API
class CRUDDataSerializer(viewsets.ModelViewSet):
    serializer_class = CRUDDataSerializer
    permission_classes = [IsAuthenticated]
    queryset = CRUDData.objects.all()


class SignupViewset(viewsets.ModelViewSet):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()


class LoginViewset(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.data["username"])
            if user is not None:
                credentials = {"username": user.username, "password": request.data["password"]}
                user = authenticate(**credentials)
                if user:
                    token, created = Token.objects.get_or_create(user=user)
                    user_data = LoginSerializer(user)
                    return Response({
                        "status": 200,
                        "message": "User Logged in successfully",
                        'token': token.key,
                        'data': user_data.data,
                    })
                else:
                    return Response({
                        "status": 200,
                        "message": "in correct pass",
                        'data': [],
                    })
        except User.DoesNotExist as e:
            raise ValueError("User does not exists")
