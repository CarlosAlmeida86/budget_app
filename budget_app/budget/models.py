from django.db import models

from django.db import models


class Transaction(models.Model):
    CATEGORY_CHOICES = (
        ('necessary', 'Gastos Necessários'),
        ('leisure', 'Lazer'),
        ('savings', 'Economia/Investimentos'),
    )

    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()

    def __str__(self):
        return self.title

    def format_date(self):
        return f"{self.date}"
