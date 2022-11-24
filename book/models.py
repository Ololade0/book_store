from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils.text import slugify
from django.urls import reverse


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()

    def get_absolute_url(self):
        return reverse("book_store:publisher-details", args=[self.id])


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


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
    edition = models.PositiveSmallIntegerField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default="R")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title
        # f"({self.price})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["title"]


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=6, validators=[MinLengthValidator(5, "code must be greater than five"),
                                                     MaxLengthValidator(6, "code cannot exceed the length six")])
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)
