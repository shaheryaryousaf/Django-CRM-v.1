from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group


# ===============================
# Custom User Manager For New User Model
# ===============================
class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, type, password=None):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, type=type)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name,last_name, type, password):
        user = self.create_user(email, first_name,last_name, type, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# ===============================
# Custom User Model For Registration
# ===============================
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()
    # Replace username field with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'type']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email