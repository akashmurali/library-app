from rest_framework import serializers
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password
#models
from customer.models import Customer
from books.models import Book

class RegisterSerializer(serializers.ModelSerializer):   
    username = serializers.CharField(max_length=100,write_only=True)
    password = serializers.CharField(max_length=100,write_only=True) 
     
    
    class Meta:
        model = Customer
        fields = (
            "name","phone","email","username","password"
        )

    def create(self,validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        name = validated_data.get('name')
        email = validated_data.get('email')

        customer = Customer.objects.create(**validated_data)        
        
        user = User.objects.create(
            first_name=name,username=username,
            email=email,
            password=make_password(password)
        )
        
        customer.user=user
        customer.save()

        customer_group, created = Group.objects.get_or_create(name='customer')
        customer_group.user_set.add(user)      

        return customer    


class BookListSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id","name","author")        