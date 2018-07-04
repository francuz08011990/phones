from django.db import models


class Phones(models.Model):
    brand = models.CharField(max_length=100)
    year_of_foundation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.brand


class Type(models.Model):
    name_of_model = models.CharField(max_length=200)
    phone = models.ForeignKey(Phones,
                               on_delete=models.CASCADE,
                               related_name='types')
    price = models.IntegerField()
    start_of_sales = models.DateField()
    image = models.ImageField()

    def __str__(self):
        return self.name_of_model

