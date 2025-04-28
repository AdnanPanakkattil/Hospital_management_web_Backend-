from django.urls import path
from . import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    path('', views.index, name='index'),
# Api

    path('DoctorsApi/', views.DoctorsApi.as_view(), name='doctorsApi'),
    path('DepartmentApi/', views.DepartmentApi.as_view(), name='departmentApi/'),
    path('ContactApi/',views.ContactApi.as_view(), name='ContactApi/'),
    path('AppoinmentApi/',views.AppoinmentApi.as_view(), name='AppoinmentApi/'),

]
   
