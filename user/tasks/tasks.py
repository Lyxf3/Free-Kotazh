# region				-----External Imports-----
import json
from django.conf import settings as django_settings
from django.db import models
from django import utils
import requests
import logging
import celery
# endregion

# region				-----Internal Imports-----
from .. import models as user_models
# endregion

# region			  -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion
