from django.db import models
from account import models as account_models

class Car(models.Model):
    name = models.CharField("Имя автомобиля", max_length=255)
  
    def __str__(self):
        return self.name

class APK(models.Model):
    user = models.ForeignKey(account_models.CustomUser, on_delete=models.CASCADE, related_name='apks')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='apks')
    apk_file = models.FileField(upload_to='apk_files/')
    created_at = models.DateTimeField("Дата загрузки", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s APK for {self.car.name}"
