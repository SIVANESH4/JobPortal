from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    job_title=models.CharField(max_length=100)
    description=models.TextField()
    location=models.CharField(max_length=100)
    salary_range=models.CharField(max_length=50, blank=True)
    company=models.CharField(max_length=100)
    posted_on=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

class Application(models.Model):
    STATUS_CHOICES = {
        ('pending', 'Pending'),
        ('shortlisted', 'ShortListed'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    }
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_on=models.DateTimeField(auto_now_add=True)

