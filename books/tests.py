from django.test import TestCase
from books.models import Book


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="Test book", author="Test author", price=1, amount=3)

    def test_book_must_have_author(self):
        test_book = Book.objects.get(title="Test book")
        self.assertEqual(test_book.author, 'Test author')
