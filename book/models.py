from django.db import models


class Book(models.Model):
    GENRE_CHOICES = (
        ("C", "Comedy"),
        ("T", "Tragedy"),
        ("TC", "Tragicomedy"),
        ("CR", "Crime"),
        ("R", "Romance"),
        ("SF", "Science Fiction")
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, default="-")
    isbn = models.CharField(max_length=20)
    date_added = models.DateField(auto_now_add=True)
    date_published = models.DateField()
    edition = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default="R")


