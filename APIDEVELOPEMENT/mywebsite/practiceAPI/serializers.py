from rest_framework import serializers
from .models import studentsinfo

class studentsSeralizer(serializers.ModelSerializer):

    class Meta:
        model = studentsinfo
        fields = "__all__"