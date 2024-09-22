from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)  # Assuming a simple string representation for the mobile number
    address = models.CharField(max_length=225)
    class Meta:
        db_table = "user_profile"

# models.py

from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f"{self.user.username}'s Cart - {self.product_name}"

# models.py

class AllFruits(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    url = models.URLField(max_length=255)

    class Meta:
        db_table = 'all_fruits2'
        unique_together = ['id', 'name']

    def __str__(self):
        return self.name
class Mango(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    category = models.CharField(max_length=50)
    categoryName = models.CharField(max_length=50)
    imgUrl = models.CharField(max_length=355)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField()
    class Meta:
        db_table='mango'

    def __str__(self):
        return self.categoryName

class ProductDetails(models.Model):
    fruitname=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField()
    imgUrl=models.CharField(max_length=300)

    class Meta:
        db_table='product_details'
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Mango, on_delete=models.CASCADE)  # Assuming you have a Mango model
    quantity = models.PositiveIntegerField()
    img_url = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     db_table='cart_items'

    def __str__(self):
        return f"{self.user.username} - {self.product.categoryName} - {self.quantity} kg"
