from django.db import models
from django.utils import timezone

# Create your models here.

class Flea_market(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(blank = True, upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title
    def summary(self): 
        return self.body[:20]
