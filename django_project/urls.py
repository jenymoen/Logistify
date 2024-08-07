"""
URL configuration for django_project project.

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
from django.urls import path
from django.contrib import admin
from logistify import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shipment_list/", views.shipment_list, name="shipment_list"),
    path('admin/', admin.site.urls),
    path('shipment_detail_view/<str:pk>/', views.shipment_detail_view, name="shipment_detail_view"),
    path('create_rfq/', views.createRFQ, name="create_rfq"),
    path('rfq_list/', views.rfq_list, name="rfq_list"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('item_list/', views.item_list, name="item_list"),
]


