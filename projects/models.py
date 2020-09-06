from django.db import models

class Project(models.Model):  # instance of class is a row
    title = models.CharField(max_length=100)  # column in database
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")