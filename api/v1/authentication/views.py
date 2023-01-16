from datetime import time
import pdb
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes ,parser_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import login ,authenticate,logout
from django.conf import settings as SETTINGS
from django.shortcuts import get_object_or_404
from api.v1.authentication.services import create_token
from api.v1.authentication.serializers import *



@api_view(['POST'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def user_login(request):
    serialized = LoginSerializer(data=request.data)
    if serialized.is_valid():
        username = serialized.validated_data['username']        
        password = serialized.validated_data['password']        
        user = authenticate(username=username, password=password)        

        if not user:

            response_data = {
                "StatusCode": 6001,
                "message": "User does not exists. Please check your username and password!"
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        else:
            login(request,user)
            token = create_token(user)
            access_life = SETTINGS.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
            group = request.user.groups.values_list('name', flat=True)

            response_data = {
                "StatusCode": 6000,                
                "data": {
                    "token": token,
                    "groups": group                    
                }
                            
            }              
            return Response(response_data, status=status.HTTP_200_OK)           

    else:
        response_data = {
            "StatusCode": 6001,
            "message":  serialized._errors
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def user_logout(request):
    logout(request)

    response_data = {
            "StatusCode": 6000,
            "message" : "Successfully Logged out "
        }

    return Response(response_data, status=status.HTTP_200_OK)