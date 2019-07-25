from django.urls import path ,include
from . import views

app_name = 'user'
urlpatterns = [
    path('users/', views.index),
    path('download/',views.csv_download,name = 'csv'),

]
