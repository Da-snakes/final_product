from django.db import models
from django.contrib.auth.models import User
from project.models import Project

# Create your models here.
# company object
class Company(models.Model):
    social_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    found_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('name',)


    def __str__(self):
        return (self.name)
# user object
class UserProfile(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, blank=True)
    img    = models.ImageField(upload_to='media', blank=True, default='core/avatar/blank_profile.png')

    def __str__(self):
        return (str(self.user))

    


