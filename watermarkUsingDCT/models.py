from django.db import models


class Qrcode(models.Model):
    Qrcodeimg = models.ImageField(upload_to='input/')

# Create your models here.
class WaterMark(models.Model): 
    #name = models.CharField(max_length=50) 
    coverImg = models.ImageField(upload_to='input/')
    watermarkImg = models.ImageField(upload_to='input/')

