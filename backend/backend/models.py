from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    job_title=models.CharField(max_length=100)
    description=models.TextField()
    location=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    posted_on=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
