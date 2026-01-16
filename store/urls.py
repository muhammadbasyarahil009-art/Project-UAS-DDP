from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('material/<int:material_id>/', views.detail, name='detail'),
    
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('employee/', views.employee, name='employee'),
]