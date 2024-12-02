from django.db import models

# This is a field that includes project (dev projects)
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    live_link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
# Skills section
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # e.g., 0-100 scale

    def __str__(self):
        return self.name
    
# contact section
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

# blog post
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
