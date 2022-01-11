from django import forms
from .models import empblog, comblog,blogger,practiceblog


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = empblog
        fields = ("emp_name", "emp_des")


class ClientForm(forms.ModelForm):
    class Meta:
        model = comblog
        fields = ("name","middle_name", "last_name", "password", "reenterpassword")

class blogform(forms.ModelForm):
    class Meta:
        model = blogger
        fields = ("name","middlename", "lastname", "password", "reenterpassword")

class blogformpractice(forms.ModelForm):
    class Meta:
        model = practiceblog
        fields = ("name","middlename","lastname")



