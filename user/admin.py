# region				-----External Imports-----
from django import (http, contrib)
from django.db import models
import typing
# endregion

# region				-----Internal Imports-----
from . import models as user_models
# endregion

# region			  -----Supporting Variables-----
# endregion


@contrib.admin.register(user_models.User)
class UserAdmin(contrib.admin.ModelAdmin):

    list_display = ["id", "phone", "username",
                    "image", "first_name",
                    "permission_level", "is_staff"]

    def save_model(self, request: http.HttpRequest,
                   obj: user_models.User,
                   change,
                   form):
        if obj.pk:
            orig_obj = user_models.User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()
