from django.db import models

class Author(models.Model):
    """
    Represents an author with a name.
    Each author can have multiple books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book with a title, publication year, and an associated author.
    The author field establishes a one-to-many relationship with the Author model.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
