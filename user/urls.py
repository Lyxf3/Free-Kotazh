# region				-----External Imports-----
# endregion

# region				-----Internal Imports-----
from .api.frontend import urls as urls
# endregion

# region			  -----Supporting Variables-----
# endregion

urlpatterns = urls.frontend_router.urls
