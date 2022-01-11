# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.views import View
# from django.contrib.auth import authenticate, logout
#

# def mno(request):
#     return HttpResponse("hello people")
#
# def stu(request):
#     return HttpResponse("hello world")
#
# def form(request):
#     return render(request,"form.html")
#
#
# class registration_from(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,'registration_from.html')
#
#
#
# class satishLogin1(View):
#     def get(self,request,*args,**kwargs):
#         return render(self.request,'satishlogin.html')
#
#     def post(self, request, *args, **kwargs):
#         data = request.POST.get
#         print(data)
#         user = authenticate(username=data("username"), password=data("password"))
#         if user is not None:
#             return redirect("satishhomelogout")
#         else:
#             return HttpResponse("soemthing went wrong")
#
# def satishlogout_user(request):
#     logout(request)
#     return redirect("loginsatish")
#
# def home1(request):
#     return render( request,"satishlogout.html",{"user":request.user.username})
#
#
#
#
#
