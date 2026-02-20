from rest_framework import serializers
from django.contrib.auth.models import User
from backend.models import *


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class JobSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Job
        fields = "__all__"

class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"