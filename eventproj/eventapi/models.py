from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Only hash the password if it hasn’t been hashed yet
        if not self.password.startswith('pbkdf2_') and self._state.adding:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    event_datetime = models.DateTimeField(null=True, blank=True)
    location = models.OneToOneField('Location', on_delete=models.CASCADE)
    Latitude = models.DecimalField(max_digits=10, decimal_places=3)
    Longitude = models.DecimalField(max_digits=10, decimal_places=3)
    Category = models.CharField(max_length=10)
    Status = models.CharField(max_length=20)
    Submitted_By = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Location(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.city}, {self.country}"