"""tutorial URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
# from myApp import apis
import sys

from myApp import apis

sys.path.append('../')
from myApp import apis
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', apis.BookViewSet)
router.register(r'users', apis.UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

#     url(r'^api/users/$', apis.UserList.as_view()),
#     url(r'^api/users/(?P<pk>[0-9]+)/$', apis.UserDetail.as_view()),
#     url(r'^api/books/$', apis.BookList.as_view()),
# url(r'^api/books/(?P<pk>[0-9]+)/$', apis.BookDetail.as_view()),
]


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]