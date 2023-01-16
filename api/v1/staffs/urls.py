from django.urls import re_path,path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from . import views
  
 
app_name = "api_v1_staff"


urlpatterns = [
    re_path(r'^register/$', views.register_staff),
    path('view-requests/', views.view_requests),
    path('validate-request/<uuid:pk>/', views.validate_request),
    



    # re_path(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # re_path(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
   
    # #password reset
    # re_path(r'^reset_username&password/$', views.reset_username_password),

    # #change password
    # re_path(r'^change-password/$', views.change_password),


   
]