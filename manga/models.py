from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(_("birth date"), blank=True, null=True)

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='media/covers')
    categories = models.ManyToManyField(Category)
    ratings = models.ManyToManyField(User, through='Rating')

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'manga')


class MangaPage(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    page_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/manga_pages')

    class Meta:
        unique_together = ('manga', 'page_number')
        ordering = ['page_number']

    def __str__(self):
        return f'{self.manga.title} - Page {self.page_number}'
