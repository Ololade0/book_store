
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

import book
from .models import Book, Publisher
from .serializers import BookSerializers, BookCreateSerializers, PublisherSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('publisher').all()



# class BookList(ListCreateAPIView):
#     queryset = Book.objects.select_related('publisher').all()
#     serializer_class = BookSerializers
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#
#
# class PublisherList(ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#
#
# class PublisherDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#
#
#




# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     if request.method == 'GET':
#         Queryset = Publisher.objects.annotate(
#             number_of_books_oublishes=Count('books')
#         ).all()
#
#         serializer = PublisherSerializer(Queryset, many=True)
#
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PATCH', 'DELETE'])
# def publisher_detail(request, pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     if request.method == 'GET':
#         serializer = PublisherSerializer(publisher)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#          serializer = PublisherSerializer(publisher, data=request.data, partial=True)
#          serializer.is_valid(raise_exception=True)
#          serializer.save()
#          return Response(serializer.data)
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
