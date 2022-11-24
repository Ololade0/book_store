from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Publisher
from .models import Book
from django.db.models import Count, Max, Min, Avg, Sum


#
# TO GET AllLIST FROM DATABSe
# def index(request):
#     queryset = Publisher.objects.all()
#     return render(request, "book/index.html", context={"publishers": list(queryset)})


# TO GET LIST FROM DATABSE
def index(request):
    queryset = Publisher.objects.filter(name="Ntag")
    return render(request, "book/index.html", context={"publishers": list(queryset)})


# TO GET ONE OBJECT
def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, "book/publisher-detail.html", context={"publisher": publisher})


# # All
# def book_list(request):
#     queryset = Book.objects.all()
#     return render(request, "book/book_list.html", context={"books": list(queryset)})
#

# ORDER
def order(request):
    queryset = Book.objects.order_by('title')
    return render(request, "book/book_list.html", context={"books": list(queryset)})

#
# # to filter
# def book_list(request):
#     queryset = Book.objects.filter(title__icontains="the")
#     return render(request, "book/book_list.html", context={"books": list(queryset)})
#
#
# # TO LIMIT WHAT TYOU NEED
# def book_list(request):
#     queryset = Book.objects.select_related("publisher").all()[10:15]
#     return render(request, "book/book_list.html", context={"books": list(queryset)})


def book_list(request):
    queryset = Book.objects.select_related("publisher").all()
    # result =  queryset.aggregate(Count('id'))
    return render(request, "book/book_list.html", context={"books": list(queryset)})
