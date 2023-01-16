from urllib import response
# import requests ,json
import pdb
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from general.decorators import group_required
import datetime
from django.contrib.auth.models import Group
#models
from books.models import Book,BookRequest
#serializers
from .serializers import *
from api.v1.books.serializers import BookSerializer


#register customer
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def register_customer(request):
    serialized = RegisterSerializer(data=request.data, context={'request': request})

    if serialized.is_valid():
        serialized.save()

        response_data = {
            "StatusCode" : 6000,
            "data" : serialized.data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    else:
        
        response_data = {
            "StatusCode" : 6001,
            "data" : serialized.errors
        }

        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

#list view of book
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@group_required("customer")
@renderer_classes((JSONRenderer,))
def view_books(request):   
    instance =  Book.objects.filter(is_deleted=False).order_by( '-date_added' )
    serialized = BookListSerailizer(
       instance,
       many=True,
       context = {
            "request": request,
        }
    )
    response_data = {
        "StatusCode": 6000,
        'data' : serialized.data,
    }

    return Response(response_data, status=status.HTTP_200_OK)


#read book
@api_view(['GET'])
@group_required("customer")
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def book_single_view(request,pk):
    user = request.user
    try:
        record =  BookRequest.objects.get(customer__user=user,book__id=pk,is_accepted=True,
                  is_completed = False)      
        
        instance = Book.objects.get(id=pk)
        data  = BookSerializer(instance).data

    except BookRequest.DoesNotExist:        
        data = "Request for Read"  
    
    response_data = {
        
        'data' : data,
    }    

    return Response(response_data,status=status.HTTP_200_OK) 


#request for book
@api_view(['GET'])
@group_required("customer")
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def request_book(request,pk):
    instance = Book.objects.get(id=pk)
    customer = Customer.objects.get(user=request.user)
    if BookRequest.objects.filter(customer=customer,book=instance,is_accepted=True,
        is_completed=False).exists():
        data = "you are eligible to read.Request already granted!"
        
    else:
        BookRequest.objects.create(book=instance,customer=customer) 
        data = "request compeleted.wait for confirmation"
    
    response_data = {
        
        'data' : data,
    }    
    return Response(response_data,status=status.HTTP_200_OK) 