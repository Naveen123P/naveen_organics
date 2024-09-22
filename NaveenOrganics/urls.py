"""
URL configuration for NaveenOrganics project.

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
from django.contrib import admin
from django.urls import path
from NaveenOrganicsApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('home3/',views.home),
    # path('test2/<str:fruitName>/',views.test2,name='test2'),

    path('FruitsTableData/mango2/', views.mango2),

    #path('login/', views.login, name='user_login'),
    path('FruitsTableData/mango/', views.mango),
    
    # path('fruitsdata/mango/<str:fruitName>/', views.fruitWiseList,name='fruitWiseList'),
    path('login/',views.login),
    path('about/', views.about),
    path('register/',views.register),
    path('mango/',views.mango),
    path('Fruits/mango/',views.mangodet),

    path('FruitsTableData/productDetails/', views.productdetails),


    path('cart/', views.add_to_cart, name='add_to_cart'),
    path('login/userDashbord/', views.dashboard),
    path('apple/',views.apple),
    path('banannas/',views.banannas),
    path('ber/',views.ber),
    path('cashew/',views.cashew),
    path('coconut/',views.coconut),
    path('custardapple/',views.custardapple),
    path('dragen/',views.dragen),
    path('fig/',views.fig),
    path('grapes/',views.grapes),
    path('guavas/',views.guavas),
    path('jackfruit/',views.jackfruit),
    path('kiwi/',views.kiwi),
    path('orange/',views.orange),
    path('papayas/',views.papayas),
    path('peach/',views.peach),
    path('pears/', views.pears),
    path('pineapple/',views.pineapple),
    path('plum/',views.plum),
    path('pomegranate/',views.pomegranate),
    path('sapota/',views.sapota),
    path('sweetLime/',views.sweetLime),
    path('logout/',views.logout),
]
