from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    vegetarian = models.BooleanField()
    ingredients = models.ManyToManyField(
        'Ingredients', related_name='ingredients', blank=True)
    custom = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Ingredients(models.Model):

    name = models.CharField(max_length=30)
    cat = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Custom_burger(models.Model):

    custom_name = models.CharField(max_length=254)
    buns = models.ManyToManyField(
        'Ingredients', related_name='buns', blank=True)
    burger = models.ManyToManyField(
        'Ingredients', related_name='burger', blank=True)
    sauce = models.ManyToManyField(
        'Ingredients', related_name='sauce', blank=True)
    salads = models.ManyToManyField(
        'Ingredients', related_name='salads', blank=True)
    cheese = models.ManyToManyField(
        'Ingredients', related_name='cheese', blank=True)
    extras = models.ManyToManyField(
        'Ingredients', related_name='extras', blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.CASCADE,
        related_name='custom_burger')
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default='10.99', editable=False)

    def __str__(self):
        return self.custom_name
