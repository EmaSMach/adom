from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='inicio'),
    path('sobrenosotros/', views.acerca, name='acerca'),

    
]
