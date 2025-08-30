# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve the specific book we created
book = Book.objects.get(title="1984")

# Display attributes
print(book.title, book.author, book.publication_year)

# Expected Output:
# 1984 George Orwell 1949
