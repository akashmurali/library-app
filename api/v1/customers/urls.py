from django.urls import re_path,path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from . import views
  
 
app_name = "api_v1_customer"


urlpatterns = [
    #register customer
    path(r'^register/$', views.register_customer),
    #book list view
    path('book-list/', views.view_books),
    path('book-single/<uuid:pk>/', views.book_single_view),
    path('request-book/<uuid:pk>/', views.request_book),
    



    # re_path(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # re_path(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
   
    # #password reset
    # re_path(r'^reset_username&password/$', views.reset_username_password),

    # #change password
    # re_path(r'^change-password/$', views.change_password),


   
]