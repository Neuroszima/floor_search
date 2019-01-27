import json, ast
from django.db import models
from django.utils import timezone


# Create your models here.

COMPANY_SIZES = (
    (1, 'small'),
    (2, "average"),
    (3, "big")
)

FLOOR_TYPES = (
    (1, "Wood"),
    (2, "Laminate"),
    (3, "Tiles"),
    (4, "Imitation"),
    (5, "Other")
)

# models to use in future


# class FloorClass(models.Model):
#     name = models.CharField(max_length=255)
#     type = models.IntegerField(choices=FLOOR_TYPES)
#
#
# class Manufacturer(models.Model):
#     name = models.CharField(max_length=255)
#     manufacturer_webpage_link = models.TextField()
#     company_size = models.IntegerField(choices=COMPANY_SIZES)
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.FloatField()
#     description = models.TextField()
#     image_link = models.TextField()
#     comments = models.TextField()
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#     type = models.ForeignKey(FloorClass, on_delete=models.CASCADE)
#
#
# class Retailer(models.Model):
#     name = models.CharField(max_length=255)
#     company_size = models.IntegerField(choices=COMPANY_SIZES)
#     retailer_webpage_link = models.TextField()
#     retailer_querry_link = models.TextField()


#following class comes from a scrapy tutorial at:
class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField()  # this stands for our crawled data
    date = models.DateTimeField(default=timezone.now)

    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id

    def data_to_list(self):
        return ast.literal_eval(self.data)
