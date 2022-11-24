from rest_framework import serializers
from .models import Book, Publisher


class PublisherSerializer(serializers.Serializer):  # noqa
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    website = serializers.URLField()


class BookSerializers(serializers.Serializer):  # noqa
    title = serializers.CharField(max_length=255)
    isbn = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    publisher = serializers.HyperlinkedRelatedField(
        queryset=Publisher.objects.all(),
        view_name="book_store:publisher-detail"
    )

    # class Meta:
    #     model = Book
    #     fields = "__all__"
    #
















    # publisher = serializers.StringRelatedField(),
    #  queryset = publisher.objects.all(
    # publisher = PublisherSerializer()

#
# def book_list(request):
#     if request.method == "Get":
#         Queryset = Book.objects
