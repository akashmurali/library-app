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
from datetime import datetime,timedelta
from django.contrib.auth.models import Group
#serializers
from .serializers import *


#register staff
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def register_staff(request):
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

        


@api_view(['GET'])
@group_required("staff")
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def view_requests(request):
    queryset =  BookRequest.objects.filter(is_deleted=False).select_related("book","customer")

    serialized_data = BookRequestSerializer(queryset,many=True).data                       
        
       
    
    response_data = {
        
        'data' : serialized_data,
    }    

    return Response(response_data,status=status.HTTP_200_OK) 


#validate request
@api_view(['PUT'])
@group_required("staff")
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def validate_request(request,pk):   
    select = request.GET.get('select')   
    if select:
        instance =  BookRequest.objects.get(id=pk)

        if instance.is_accepted:
            data = 'already accepted'

        else:    

            if select == 'accept':
                instance.is_accepted = True
                instance.start_time =  datetime.now()
            
            else:
                instance.is_accepted = False
                instance.start_time = None    
    
            instance.save()
            data = BookRequestSerializer(instance).data                       
        
    else:
        data = 'please accept or decline the request!'   
    
    response_data = {
        
        'data' : data,
    }    

    return Response(response_data,status=status.HTTP_200_OK)