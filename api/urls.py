# from django.conf.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('paises', views.PaisAPI)
# router.register('paises/<int:pk>/provincias', views.ProvinciaAPI)
# router.register(r'addresses', views.AddressAPI)
# router.register(r'medias', views.MediasAPI)

urlpatterns = router.urls
# api_login_pattern = url(r'login/$', views.login, name='api-login')
# urlpatterns.append(api_login_pattern)
