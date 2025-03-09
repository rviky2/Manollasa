from django.db import models


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class course(models.Model):
    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    Eligibility = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class apply(models.Model):
    Name = models.CharField(max_length=100, blank=True, default='nothing')
    Email = models.CharField(max_length=100, default='nothing')
    Place = models.CharField(max_length=100, blank=True, default='nothing')
    Phone = models.CharField(max_length=100, blank=True, default='nothing')
    Branch = models.CharField(max_length=10, blank=True, default='nothing')
    date = models.DateField()

    def __str__(self):
        return self.Name
