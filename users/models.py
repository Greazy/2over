from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
