"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1.views import mainPage
from app1.views import aboutPage, coursePage, enquiry, viewEnquiries
from app1.views import editEnquiry, deleteEnquiry
from app1.views import AddStudent, ViewStudents, EditStudent, DeleteStudent
from app1.views import signup, staffPage
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainPage,name='main'),
    path('about/',aboutPage,name='about'),
    path('course/',coursePage,name='cour'),
    path('enq/',enquiry,name='enquiry'),
    path('view/',viewEnquiries,name='viewEnq'),
    path('view/update/<id>/',editEnquiry,name='editEnq'),
    path('view/delete/<id>/',deleteEnquiry,name='delEnq'),

    path('addStudent/',AddStudent.as_view(),name='addStu'),
    path('viewStudent/',ViewStudents.as_view(),name='viewStu'),
    path('viewStudent/editStudent/<id>/',EditStudent.as_view(),name='editStu'),
    path('viewStudent/delStudent/<id>/',DeleteStudent.as_view(),name='delStu'),

    path('staff/',staffPage,name='staff'),
    path('signup/',signup,name='sign'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='main'),name='logout'),

    path('password_reset/',PasswordResetView.as_view(template_name='passwordReset.html'),name='password_reset'),
    path('passwordDone/',PasswordResetDoneView.as_view(template_name='resetDone.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='resetConfirm.html'),name='password_reset_confirm'),
    path('resetComplete/',PasswordResetCompleteView.as_view(template_name='resetComplete.html'),name='password_reset_complete')

]
