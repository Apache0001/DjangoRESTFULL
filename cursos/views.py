from rest_framework import generics
from .models import Curso, Avaliacao
from.serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import permissions

from .permissions import EhSuperUser


class CursosAPIView(generics.ListCreateAPIView):
    throttle_scope = 'cursos'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
        )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    

class AvaliacoesAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Avaliacao.objects.all()
    serializer_class  = AvaliacaoSerializer

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
