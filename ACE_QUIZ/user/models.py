from django.db import models

# Create your models here.

class AbstractUserClass(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.URLField(max_length=200)

    def formalName(self):
        return self.first_name + ' ' + self.last_name