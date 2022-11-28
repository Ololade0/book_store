from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views

app_name = "book_store"

router = DefaultRouter()
router.register('books', viewset=views.BookViewSet, basename='book')
router.register('publishers', viewset=views.PublisherViewSet, basename='publisher')

urlpatterns = router.urls
