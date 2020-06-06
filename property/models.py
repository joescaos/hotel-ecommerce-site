from django.db import models

property_type = (
    ('Sale', 'sale'),
    ('Rent', 'rent'),
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True)
    property_type = models.CharField(choices = property_type, max_length=10)
    price = models.PositiveIntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Reserve(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name

