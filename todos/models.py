from django.db import models

# Create your models here.
class ParsonalTodo(models.Model):
  title = models.CharField(max_length=20)
  complate = models.BooleanField(default=False)
  listtime = models.TimeField(auto_now=True)
  createDate = models.DateField(auto_now_add=True)
  


  