from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    is_activated=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Brands(models.Model):
    brand_name=models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name

class Products(models.Model):
    name=models.CharField(max_length=200)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    condition=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    option=(
        ("for_sale","for_sale"),
        ("exchange","exchange"),
        ("sold","sold"),
        ("rent","rent")
    )        
    status=models.CharField(max_length=200,choices=option,default="for_sale")
    created_date=models.DateField(auto_now_add=True)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    image=models.ImageField(null=True,upload_to="products.images")        

class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(null=True,upload_to="profile.images")
    address=models.CharField(max_length=200)
    mobile=models.PositiveBigIntegerField()

class Notification(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    options=(
        ("sent","sent"),
        ("cancelled","cancelled"),
        ("pending","pending")
    )
    status=models.CharField(max_length=200, choices=options, default="sent")