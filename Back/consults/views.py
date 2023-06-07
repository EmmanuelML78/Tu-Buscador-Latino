from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Consulta
from .serializers import ConsultaSerializer
from django.utils import timezone
import requests
from bs4 import BeautifulSoup

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

        url = f"https://es.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={palabra_buscada}"
        response = requests.get(url)
        data = response.json()

        # Obtener los resultados de la API
        results = data['query']['search']

        filtered_results = []
        for result in results:
            pageid = result['pageid']
            title = result['title']
            snippet_html = result['snippet']

            # Eliminar etiquetas HTML 
            soup = BeautifulSoup(snippet_html, 'html.parser')
            snippet_text = soup.get_text()

            filtered_results.append({
                'pageid': pageid,
                'title': title,
                'snippet': snippet_text,
            })

        return Response(filtered_results)

class ConsultaListView(ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
