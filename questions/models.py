from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=100)
    ##question = models.CharField(max_length=100,unique=True)---used to eliminate duplicates
    category = models.CharField(max_length=100)
    ##category = models.CharField(max_length=100,blank=True,Null=True)
    #category = models.CharField(max_length=100,default='others')---default option
    added_dt = models.DateTimeField(auto_now_add=True)