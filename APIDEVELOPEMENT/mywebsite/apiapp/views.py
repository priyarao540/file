from django.shortcuts import render
from rest_framework import viewsets
from .serializers import photographySerializer
from.models import photography


class photographyviewset(viewsets.ModelViewSet):
    queryset=photography.objects.all().order_by('Camera_name')
    serializer_class=photographySerializer

# Create your views here.
