from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie
# Create your views here.

class ModelViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(typ='action')
    serializer_class=MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(typ='comedy')
    serializer_class=MovieSerializer
