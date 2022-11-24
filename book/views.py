from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Publisher
from .serializers import BookSerializers
from .serializers import PublisherSerializer


@api_view()
def book_list(request):
    Queryset = Book.objects.select_related('publisher').all()
    serializer = BookSerializers(Queryset, many=True, context={"request" : request})
    return Response(serializer.data)


@api_view()
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializers(book)
    return Response(serializer.data)


@api_view()
def publisher_list(request):
    Queryset = Publisher.objects.all()
    serializer = PublisherSerializer(Queryset, many=True)

    return Response(serializer.data)


@api_view()
def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    serializer = PublisherSerializer(publisher)
    return Response(serializer.data)
