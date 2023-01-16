from django.urls import re_path,path
from api.v1.authentication import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = "api_v1_authentication"


urlpatterns = [
    #token
    re_path(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    #common login
    re_path(r'^login/$', views.user_login),
    #common logout
    re_path(r'^logout/$', views.user_logout),

    
   
      

]    