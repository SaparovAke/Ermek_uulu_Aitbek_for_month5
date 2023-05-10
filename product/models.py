from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,
                                 blank=True, related_name='products_category')
    price = models.IntegerField()
    def __str__(self):
        return self.title

class Review(models.Model):
        text = models.TextField()
        stars = models.IntegerField(blank=True, validators=[MaxValueValidator(5), MinValueValidator(1)], default=1)
        product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                    related_name='products_reviews')

        def __str__(self):
            return self.text
