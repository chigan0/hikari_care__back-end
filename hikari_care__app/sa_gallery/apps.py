from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SaGalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sa_gallery'
    verbose_name = _("Gallery")
