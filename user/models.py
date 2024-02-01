from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Viewers(models.Model):
    User = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='user/images/')
    mobile_no = models.CharField(max_length=12)

    def __str__(self):
        return self.User.username
    class Meta:
         verbose_name_plural = "Viewers"

class Editors(models.Model):
    User = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='user/images/')
    mobile_no = models.CharField(max_length=12)

    def __str__(self):
        return self.User.username
    class Meta:
         verbose_name_plural = "Editors"
