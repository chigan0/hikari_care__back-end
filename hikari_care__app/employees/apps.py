from django.apps import AppConfig
from django.utils.translation import get_language, gettext_lazy as _

class EmployeesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "employees"
    verbose_name = _("Персонал")
 