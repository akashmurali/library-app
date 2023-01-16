from unicodedata import category
from urllib import request
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User,Group
from django.db.models.base import Model
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length= 100)
    password = serializers.CharField(max_length = 100,write_only=True)        