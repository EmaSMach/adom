from django.urls import path, include
from myapps.trabajadores import views
from django.views.generic import ListView, CreateView, DetailView, UpdateView



urlpatterns = [
    path('trabajadores/', views.PostListView.as_view(), name='trabajadores'),
    path('crear/', views.postear_oferta, name='crear_post'),
    path('<int:pk>/detalles/', views.PostDetailView.as_view(), name='detalles_post'),
    path('<int:pk>/editar/', views.PostUpdateView.as_view(), name='editar_post'),
]

