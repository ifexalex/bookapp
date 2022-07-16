from django.shortcuts import render
from rest_framework import viewsets
from.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    http_method_names = ['get', 'post', 'put']
