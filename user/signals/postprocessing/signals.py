# region				-----External Imports-----
from utils.generate_code import generate_auth_code as utils_generate_code
from utils.first_party import signals as utils_signals
from django.db.models import signals
from django import dispatch
import logging
import typing
import celery
# endregion


# region				-----Internal Imports-----
from ... import models as user_models

# endregion

# region			  -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion
