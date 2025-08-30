# Update Book

```python
from bookshelf.models import Book

# Retrieve the specific book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title, updated_book.author, updated_book.publication_year)

# Expected Output:
# Nineteen Eighty-Four George Orwell 1949
