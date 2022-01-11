

from rest_framework import serializers
from .models import *


class photographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=photography
        fields = '__all__'