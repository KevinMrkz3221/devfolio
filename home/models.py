from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    class Meta:
        ordering = ['-level']

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/projects', blank=True, null=True)
    url = models.URLField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name