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
from rest_framework.views import APIView
from general.decorators import group_required
from django.utils.decorators import method_decorator
#models
from books.models import Book as BookModel

#serializers
from .serializers import *


#register customer

class Book(APIView):    
    permission_classes = [IsAuthenticated]

       
    def get_object(self, pk):
        try:
            return BookModel.objects.get(pk=pk)
        except BookModel.DoesNotExist:
            raise Http404
    
    
    def get(self, request, pk=None):
        if pk:
            book = self.get_object(pk)
            serializer = BookSerializer(book)

        else:   
            books = BookModel.objects.all()
            serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


    
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.is_deleted = True
        book.save()
        return Response(status=status.HTTP_204_NO_CONTENT)    