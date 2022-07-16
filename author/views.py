from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    http_method_names = ['get', 'post', 'put']
