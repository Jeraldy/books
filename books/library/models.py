from django.db import models
from django.utils import timezone

class Books(models.Model):
    CAT = (
        ('N', 'Notes/slides'),
        ('A', 'Assignments'),
        ('B', 'Biology'),
        ('C', 'Chemesry'),
        ('M', 'Mathemetics'),
        ('P', 'Physics'),
        ('O', 'Other'),
    )
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=1,choices=CAT,default='N')
    book = models.FileField(upload_to='library/static/files/')