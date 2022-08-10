# region				-----External Imports-----
from phonenumber_field import modelfields as phone_field
from django.utils import timezone
from django.contrib import auth
from django.db import models
import typing
# endregion

# region				-----Internal Imports-----
from . import managers as user_managers
from . import choices as user_choices
# endregion

# region			  -----Supporting Variables-----
# endregion


class User(auth.models.AbstractBaseUser,
           auth.models.PermissionsMixin):
    # region       -----Private Information-----
    permission_level = models.PositiveIntegerField(choices=user_choices.permission_levels,
                                                   verbose_name="permission_level",
                                                   default=1)

    is_active = models.BooleanField(verbose_name="is_active",
                                    default=True)

    is_staff = models.BooleanField(verbose_name="is_staff",
                                   default=False)

    password = models.CharField(verbose_name="password",
                                max_length=255,
                                blank=False,
                                null=True)
    # endregion

    # region              -----Information-----
    second_name = models.CharField(verbose_name="second_name",
                                   max_length=90,
                                   blank=False,
                                   null=True)

    first_name = models.CharField(verbose_name="first_name",
                                  max_length=90,
                                  blank=False,
                                  null=True)

    email = models.EmailField(verbose_name="Почта",
                              unique=True,
                              blank=False,
                              null=False)

    phone = phone_field.PhoneNumberField(verbose_name="phone",
                                         blank=False,
                                         null=False)
    # endregion

    # region                -----Relation-----
    # endregion

    # region              -----Metas-----
    class Meta(object):
        verbose_name_plural = "Users"
        verbose_name = "User"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("phone", )
    # endregion

    # region         -----Default Methods-----
    def __str__(self) -> str:
        return f"{self.phone}"
    # endregion

    # region             -----Manager-----
    objects = user_managers.CustomAccountManager()
    # endregion