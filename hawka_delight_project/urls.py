"""hawka_delight_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts_app.views import index, logout
from restaurant_app.views import show_test, get_reviews, review_detail, create_edit_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('test/', show_test),
    path('reviews/', get_reviews, name='get_reviews'),
    path("reviews/<pk>", review_detail),
    path("reviews/form/<pk>", create_edit_review),
]
