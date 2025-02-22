from bookshelf.models import Book

book = Book.objects.create(title='1984', author='George Orwell', publication_yea
r=1949)

print(book)
