from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
import os


#User Management
class MyUserManager(BaseUserManager):
    use_in_migrations: True

    #Create User
    def create_user(self, email, contact, password, **extra_fields):
        if not email:
            return ValueError("User must have an email addresss")
        
        now = timezone.now()

        user = self.model(
            email = self.normalize_email(email),
            contact=contact,
            date_joined = now,
            last_login = now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    #Create Superuser
    def create_superuser(self, email, contact, password):
        user = self.create_user(
            email=self.normalize_email(email),
            contact=contact,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


#User Model
class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, verbose_name="Email")
    fname = models.CharField(max_length=30, verbose_name="First Name")
    lname = models.CharField(max_length=30, verbose_name="Last Name")
    dob = models.CharField(max_length=30, verbose_name="D.O.B")
    gender = models.CharField(max_length=10, verbose_name="Gender")
    state = models.CharField(max_length=100, verbose_name="State")
    constituency = models.CharField(max_length=100, verbose_name="Constituency")
    contact = models.IntegerField(unique=True, verbose_name="Contact")
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_voter = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['contact']

    objects = MyUserManager()

    def __str__(self):
        return self.fname + " - " + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
