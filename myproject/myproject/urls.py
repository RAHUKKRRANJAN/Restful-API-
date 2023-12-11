"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
# from django.urls import path, include
# from users.views import DeveloperRegisterView, YourAPIListView

# urlpatterns = [
#     path('register/', DeveloperRegisterView.as_view(), name='developer-register'),
#     path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
#     path('api/', YourAPIListView.as_view(), name='api-list'),
#     # Add other URLs for OAuth2.0 token endpoints, etc.
# ]

