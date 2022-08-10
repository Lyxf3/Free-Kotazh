# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models
# endregion


class CustomAccountManager(models.BaseUserManager):

    def create_superuser(self, username, phone, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(username, phone, password, **other_fields)

    def create_user(self, username, phone, password, **other_fields):
        user = self.model(username=username, phone=phone, **other_fields)
        user.set_password(password)
        user.save()
        return user
