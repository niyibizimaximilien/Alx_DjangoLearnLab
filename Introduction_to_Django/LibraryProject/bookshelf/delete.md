# Delete Book

```python
from bookshelf.models import Book

# Retrieve the specific book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []>
