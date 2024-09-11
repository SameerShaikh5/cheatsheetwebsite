from django.db import models


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.course_name} ({self.topic})"
    
    