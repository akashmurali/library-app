from rest_framework import serializers
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password
#models
from staff.models import Staff
from books.models import BookRequest

class RegisterSerializer(serializers.ModelSerializer):   
    username = serializers.CharField(max_length=100,write_only=True)
    password = serializers.CharField(max_length=100,write_only=True) 
     
    
    class Meta:
        model = Staff
        fields = (
            "name","phone","email","username","password"
        )

    def create(self,validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        name = validated_data.get('name')
        email = validated_data.get('email')

        staff = Staff.objects.create(**validated_data)        
        
        user = User.objects.create(
            first_name=name,username=username,
            email=email,
            password=make_password(password)
        )
        
        staff.user=user
        staff.save()

        staff_group, created = Group.objects.get_or_create(name='staff')
        staff_group.user_set.add(user)      

        return staff   


class BookRequestSerializer(serializers.ModelSerializer):
    book_name = serializers.SerializerMethodField()
    customer_name  = serializers.SerializerMethodField()

    def get_book_name(self,instance):
        return instance.book.name

    def get_customer_name(self,instance):
        return instance.customer.name

    class Meta:
        model = BookRequest
        fields = '__all__' 