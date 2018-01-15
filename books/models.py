from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def create(self, title, author, description, price, amount):
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.amount = amount
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
