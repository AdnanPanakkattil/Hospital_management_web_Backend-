from django.urls import path
from . import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    path('', views.index, name='index'),

    path('DepartmentApi/', views.DepartmentApi.as_view(), name='department-list-create'),
    path('DepartmentApi/<int:id>/', views.DepartmentApi.as_view(), name='department-detail-update-delete'),

    path('DoctorsApi/', views.DoctorsApi.as_view(), name='Doctors-list-create'),
    path('DoctorsApi/<int:id>/', views.DoctorsApi.as_view(), name='Doctors-detail-update-delete'),
# Api

    path('DoctorsApi/', views.DoctorsApi.as_view(), name='doctorsApi'),
    path('DepartmentApi/', views.DepartmentApi.as_view(), name='departmentApi/'),
    path('ContactApi/',views.ContactApi.as_view(), name='ContactApi/'),
    path('AppoinmentApi/',views.AppoinmentApi.as_view(), name='AppoinmentApi/'),

]
   
