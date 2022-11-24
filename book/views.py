from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer


@api_view()
def book_list(request):
    return Response("Hello Api")