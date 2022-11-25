from django.urls import path
from . import old_views, views
from rest_framework.decorators import api_view

app_name = "book_store"

# urlpatterns = [
#     path("", views.index, name="book-list"),
#     path('<int:pk>/', views.publisher_details, name='publisher-details'),
#     path("books/", views.book_list, name="books-book-list")
# ]


urlpatterns = [
    path("books/", views.BookList.as_view(), name="bool_list"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book-details"),
    path("publishers/", views.PublisherList.as_view(), name="publisher-list"),
    path("publishers/<int:pk>/", views.PublisherDetail.as_view(), name="publisher-detail")
]