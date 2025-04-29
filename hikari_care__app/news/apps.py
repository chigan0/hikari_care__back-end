from django.apps import AppConfig
from django.utils.translation import get_language, gettext_lazy as _

class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "news"
    verbose_name = _("Медиа")