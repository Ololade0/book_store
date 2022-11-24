from rest_framework.response import Response
from .models import Book

def book_list(request):
    if request.method == "Get":
        Queryset = Book.objects