from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
     path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
path('verify',views.verify,name='verify'),
path('newuser',views.newuser,name='newuser'),
path('savefeedback',views.savefeedback,name='savefeedback')
    ]
