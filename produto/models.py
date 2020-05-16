from django.db import models
# Create your models here.
class Produto(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    description = models.CharField(max_length=100)
    link = models.URLField(max_length=1000, null=True, blank=True)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
   #image = models.ImageField(upload_to='static/', null=True, blank=True)

    def __str__(self):
        return self.title

