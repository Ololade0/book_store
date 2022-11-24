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
    path("books/", views.book_list, name="bool_list"),
    path("books/<int:pk>/", views.book_detail, name="book-details"),
    path("publishers/", views.publisher_list, name="publisher-list"),
    path("publishers/<int:pk>/", views.publisher_detail, name="publisher-detail")
]