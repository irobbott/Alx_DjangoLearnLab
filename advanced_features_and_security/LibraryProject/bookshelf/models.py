from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        user = self.create_user(username=username, email=email, password=password, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username