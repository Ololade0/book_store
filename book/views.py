from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


from .filter import BookFilter
from .models import Book, Publisher
from .serializers import BookSerializers, PublisherSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('publisher').all()
    serializer_class = BookSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title']
    ordering_fields = ['title']


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

