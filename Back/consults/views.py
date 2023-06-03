from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Consulta
from .serializers import ConsultaSerializer
from django.utils import timezone

class ConsultaView(APIView):
    def post(self, request):
        palabra_buscada = request.data.get('palabra_buscada')

        # Convertir la palabra ingresada a minúsculas y luego capitalizar la primera letra
        palabra_buscada = palabra_buscada.lower().capitalize()

        consultas = Consulta.objects.filter(palabra_buscada__iexact=palabra_buscada)

        if consultas.exists():
            # Hay consultas que coinciden, actualizar la primera consulta encontrada
            consulta = consultas.first()
            consulta.cantidad_busquedas += 1
            consulta.ultima_busqueda = timezone.now()
            consulta.save()
        else:
            # No se encontraron consultas que coincidan, crear una nueva consulta
            consulta = Consulta.objects.create(
                palabra_buscada=palabra_buscada,
            )

        return Response({'message': 'Consulta registrada correctamente.'})

class ConsultaListView(ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
