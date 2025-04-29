from django.apps import AppConfig


class SaModeltranslaterConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'sa_modeltranslater'

	verbose_name = "Sa modeltranslater"

	def ready(self) -> None:
		from .models import handle_translation_registrations

		handle_translation_registrations()