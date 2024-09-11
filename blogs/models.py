from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=200)
    body = RichTextField(config_name='default')
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
