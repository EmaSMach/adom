# from django.shortcuts import render

# from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
# from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, SAFE_METHODS, BasePermission
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


from .serializers import (PaisSerializer, ProvinciaSerializer,
                            LocalidadSerializer)
from myapps.cuentas.models import Pais, Provincia, Localidad

# Create your views here.

class ReadOnly(BasePermission):
    """Para dar permisos de solo lectura"""
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class PaisAPI(viewsets.ModelViewSet):
    """
    An api view for the address data.
    """
    permission_classes = [ReadOnly]
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    http_method_names = ('get',)



class ProvinciaAPI(viewsets.ModelViewSet):
    """
    An api view for the address data.
    """
    permission_classes = [ReadOnly]
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    http_method_names = ('get',)

    # def get(self, request):
    #     if request.GET.get('pk'):
    #         print(request.values)
    #         provincias = Provincia.objects.all().filter(pais.id == request.pk)
    #         return Response(provincias)

# from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
# from rest_framework.response import Response
# from rest_framework.views import APIView



# class ExampleView(APIView):
#     permission_classes = [IsAuthenticated|ReadOnly]

#     def get(self, request, format=None):
#         content = {
#             'status': 'request was permitted'
#         }
#         return Response(content)