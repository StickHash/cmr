"""cmr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from login import views as lviews
from content import views as cviews
from rest_framework_swagger import views as swviews

urlpatterns = [
                  path('', lviews.auth_user, name='home'),
                  path('admin/', admin.site.urls),
                  path('login/', lviews.user_login, name='login'),
                  path('logout/', lviews.user_logout, name='logout'),
                  path('recettes/', cviews.recipe_list, name='recipes'),
                  path('api/docs/', swviews.get_swagger_view()),
                  path('api/', include('api.urls')),
                  path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
