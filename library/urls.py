from django.contrib import admin
from django.urls import path, include, re_path
# from django.views.static import serve
# from django.conf import settings
from api.v1.books import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('web.urls', namespace='web')),
     path('api/v1/authentication/', include('api.v1.authentication.urls', namespace='web')),
    path('api/v1/customers/', include('api.v1.customers.urls', namespace='api_v1_customer')),
    path('api/v1/staffs/', include('api.v1.staffs.urls', namespace='api_v1_users')),
    path('api/v1/books/', views.Book.as_view()),
    path('api/v1/books/<uuid:pk>/', views.Book.as_view())
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_FILE_ROOT}),
]








