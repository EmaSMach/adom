from rest_framework import serializers

from myapps.cuentas.models import Pais, Provincia, Localidad



# class DomicilioSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     Serialize the user data.
#     """
#     # localidad = LocalidadSerializer(many=True)
#     # socials = MediasSerializer(many=True)

#     class Meta:
#         model = Domicilio
#         fields = [
#             'calle',
#             'numero_calle',
#             'manzana',
#             'parcela',
#             'barrio',
#             # 'localidad',
#         ]

class LocalidadSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para el modelo Localidad.
    """
    class Meta:
        model = Localidad
        fields = ('id', 'nombre')


class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para el modelo Provincia.
    """
    localidades = LocalidadSerializer(many=True)
    class Meta:
        model = Provincia
        fields = ('id', 'nombre', 'localidades')


class PaisSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para el modelo País.
    """
    provincias = ProvinciaSerializer(many=True)
    class Meta:
        model = Pais
        fields = ('id', 'nombre', 'provincias')

