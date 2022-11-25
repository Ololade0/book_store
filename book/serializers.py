from decimal import Decimal

from rest_framework import serializers
from .models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):  # noqa
    number_of_books_published = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'email', 'website', 'number_of_books_published']


class BookSerializers(serializers.ModelSerializer):  # noqa
    # title = serializers.CharField(max_length=255)
    # isbn = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name="book_store:publisher-detail"
    # )
    # discounted_price = serializers.SerializerMethodField(method_name="discount", read_only=True)

    def discount(self, book):
        return book.price * Decimal("0.8")

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'genre', 'price', 'publisher']


class BookCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'genre', 'price', 'date_published', 'edition', 'publisher']

