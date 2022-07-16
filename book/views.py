from django.shortcuts import render
from rest_framework import viewsets
from.serializers import BookSerializer
from.models import Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    http_method_names = ['get', 'post', 'put']

    def get_queryset(self):
        return Book.objects.all()