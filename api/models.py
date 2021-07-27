from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

class Bro(models.Model):
  name = models.CharField(max_length=200)
  style = models.CharField(max_length=100)
  lines = models.IntegerField()
  stanzas = models.IntegerField()
  def __str__(self):
    return self.name