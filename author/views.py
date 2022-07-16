from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes =(AllowAny,)

    def get_queryset(self):
        return Author.objects.all()
