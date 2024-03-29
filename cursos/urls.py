from django.urls import path

from .views import CursoAPIView, AvaliacaoAPIView, AvaliacoesAPIView, CursosAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name="curso"),
    path('avaliacoes/<int:pk>', AvaliacaoAPIView.as_view(), name="avaliacao")
]

