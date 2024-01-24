from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Car(models.Model):
    name = models.CharField("Имя автомобиля", max_length=255)
  
    def __str__(self):
        return self.name


class APK(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='apks')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='apks')
    apk_file = models.FileField(upload_to='apk_files/')

    def __str__(self):
        return f"{self.user.username}'s APK for {self.car.name}"
