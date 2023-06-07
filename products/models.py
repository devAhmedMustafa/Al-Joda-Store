from django.db import models
from users.models import CustomUser as User
from django.template.defaultfilters import slugify

class Category(models.Model):

    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True) # type: ignore

    def save(self, *args, **kwargs):
        if not self.slug:
            print(self.name)
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)
    left = models.IntegerField()
    image = models.ImageField(upload_to='images/%y/%m/%d', null=True)
    details = models.JSONField(null=True)
    discount = models.FloatField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True) # type: ignore

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.left == 0:
            self.in_stock = False
            
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class NewArrival(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class Rating(models.Model):

    stars = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    