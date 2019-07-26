"""classManagementSystem URL Configuration

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
from django.urls import path
from student import views
from student.views import StudentsSearchListView, GenderView, ModalView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.student, name="new"),
    path('all/', views.all, name="all"),
    path('', views.show, name="show"),
    path('search/', StudentsSearchListView.as_view(), name="search"),
    path('gender/', GenderView.as_view(), name="gender"),
    path('add/', views.add, name="add"),
    path('modal/', ModalView.as_view(), name="modal"),
    path('edit/<int:sid>', views.edit),
    path('delete/<int:sid>', views.destroy),
    path('update/<int:sid>', views.update),
]
