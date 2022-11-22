from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Publisher


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

# Create your views here.
