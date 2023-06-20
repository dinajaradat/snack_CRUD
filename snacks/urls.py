"""
URL configuration for snack_tracker_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import home_view_Page , SnackListView  , SnackDetailView  , SnackCreateView  ,SnackUpdateView  , SnackDeleteView 

urlpatterns = [
    path('', home_view_Page.as_view(),name = 'home'),
    path('snack_list', SnackListView .as_view(),name = 'snacks'),
    path('<int:pk>/',SnackDetailView.as_view(), name="snack_detail"),
    path('create/',SnackCreateView.as_view(), name="snack_create") , 
    path('update/<int:pk>',SnackUpdateView.as_view(), name="snack_update"), 
    path('delete/<int:pk>',SnackDeleteView.as_view(), name="snack_delete")
   
]
