from django.db import models

# Create your models here.


class FoodDetail(models.Model):
    food_id = models.AutoField
    food_name = models.CharField(max_length=40, default='')
    description_food = models.CharField(max_length=100, default='')
    date_delivery = models.DateField(auto_created=True)
    image = models.ImageField(upload_to="shop/images", default="")
    fresh = models.BooleanField('fresh', default='not fresh')

    def __str__(self):
        return self.food_name
