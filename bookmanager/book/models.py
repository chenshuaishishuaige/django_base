from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name=models.CharField(max_length=10)

class PeopelInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    #外鍵
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)