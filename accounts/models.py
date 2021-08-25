from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    description = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
    ('Pending', 'Pending'),
    ('Out for Delivery', 'Out for Delivery'),
    ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name + ' ' + self.product.name
