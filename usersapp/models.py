# from django.db import models
#
# #
# # # Create your models here.
# #
# #
# # class UzumUser(models.Model):
# #     name = models.CharField(max_length=32)
# #     surname = models.CharField(max_length=32)
# #     age = models.IntegerField()
# #     email = models.EmailField()
# #     phone = models.IntegerField(unique=True)
# #
# #
# #
# #     def __str__(self):
# #         return self.name
# #
# # class User(models.Model):
# #     username = models.CharField(max_length=100, unique=True)
# #     password = models.CharField(max_length=255)
# #     last_name = models.CharField(max_length=100, blank=True, null=True)  # Yangi maydon
# #
# #     def __str__(self):
# #         return self.username
#
#
#
#
# #
# # class User(models.Model):
# #     username = models.CharField(max_length=100, unique=True)
# #     password = models.CharField(max_length=255)
# #     last_name = models.CharField(max_length=100)
# #
# #     def __str__(self):
# #         return self.username
#
#
#
# #
# #
# # class (models.Model):
# #     username = models.CharField(max_length=100, unique=True)
# #     password = models.CharField(max_length=255)
# #     last_name = models.CharField(max_length=100)
# #     phone_number = models.CharField(max_length=100)
# #
# #     def __str__(self):
# #         return self.username
#
#
#
# class Resource(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#



from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username




#12345678654325y6i75456u6y5
from django.db import models
from django.utils.timezone import now
from threading import Timer

class AdminStatus(models.Model):
    status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def set_false_after_delay(self):
        Timer(5, self.set_status_false).start()

    def set_status_false(self):
        self.status = False
        self.save()

    def save(self, *args, **kwargs):
        if self.status:  # Agar status True bo'lsa, 5 soniyadan keyin False qilamiz
            self.set_false_after_delay()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Status: {self.status}"
