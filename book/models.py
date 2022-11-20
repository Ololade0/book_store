from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


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


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=6, validators=[MinLengthValidator(5, "code must be greater than five"),
                                                     MaxLengthValidator(6, "code cannot exceed the length six")])
