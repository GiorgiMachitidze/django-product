from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=10, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, verbose_name="Title")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    stock = models.IntegerField(verbose_name="Stock")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Products"
