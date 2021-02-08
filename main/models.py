from django.db import models

# Create your models here.
class Page_details(models.Model):
    info_name = models.CharField(blank='False',max_length=200)
    detail = models.TextField(blank='False')
    img = models.ImageField(blank='True')


    def __str__(self):
    	return self.info_name
