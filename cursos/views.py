#Importacoes do rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Importacoes dos modelos
from .models import Curso, Avaliacao
#Importacoes dos Serializes vinculados aos modelos
from .serializers import CursoSerializer, AvaliacaoSerializer
# Create your views here.

class CursoAPIView(APIView):
    """
    API de Cursos da Geek
    """

    def get(self, request):
        #Estamos no request
        #Método de acesso Get(mostrar pro cliente)
        cursos = Curso.objects.all() #pegando todos os dados do model Cursos
        serializer = CursoSerializer(cursos, many=True) #Informando a variável de busca e para pegar muitos dados. Lembre-se que o get ele pode ser usado tanto para um registro como para vários
        return Response(serializer.data) #enviando na solicitação os dados do serializer, formato padrão é o JSON do response

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"msg": "Criou com sucesso!"},serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de avaliações da Geek
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)