from django.urls import path
from . import views

app_name = "job"

urlpatterns = [
    path('', views.applications, name='list'),
    path('<int:pk>/', views.app_detail, name='detail'),
]
