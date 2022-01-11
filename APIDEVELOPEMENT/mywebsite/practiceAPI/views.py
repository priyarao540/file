from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from .models import studentsinfo
from .serializers import studentsSeralizer
from rest_framework import status
from rest_framework import generics, status, viewsets

from rest_framework.response import Response

# Create your views here.


@api_view(['GET', 'POST']) ##function based api##
def mytestcrud(request):
    if request.method == 'GET':
        snippets = studentsinfo.objects.all()
        serializer = studentsSeralizer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = studentsSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def abc(self):
    return HttpResponse("HOME.html")