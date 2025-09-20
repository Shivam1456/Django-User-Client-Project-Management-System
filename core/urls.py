from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # For token login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Optional browsable API
    path('login/', obtain_auth_token),  # POST username/password to get token
    path('', include('api.urls')),  # Include app urls
]
