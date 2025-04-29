import os
from typing import Any
from importlib import import_module
from pathlib import Path

from django.apps import apps
from django.conf import settings
from django.utils.module_loading import module_has_submodule

def autodiscover() -> None:
	for app_config in apps.get_app_configs():
		trans_file = Path(app_config.path) / "translation.py"

		if not trans_file.is_file():
			continue

		module_name = f"{app_config.name}.translation"

		try:
			import_module(module_name)
		except ImportError as e:
			# Если модуль физически существует, но ошибка всё равно есть — поднимаем
			if module_has_submodule(app_config.module, "translation"):
				raise

			# Если DEBUG — логируем, но не падаем
			if settings.DEBUG:
				print(f"[autodiscover] translation.py для '{app_config.name}' найден, "
					f"но не удалось импортировать: {e}")

	if settings.DEBUG:
		print(f"[autodiscover] Все доступные translation.py загружены. [pid: {os.getpid()}]")


def handle_translation_registrations(*args: Any, **kwargs: Any) -> None:
	from .settings import ENABLE_REGISTRATIONS

	if not ENABLE_REGISTRATIONS:
		# If the user really wants to disable this, they can, possibly at their
		# own expense. This is generally only required in cases where other
		# apps generate import errors and requires extra work on the user's
		# part to make things work.
		return

	# Trigger autodiscover, causing any TranslationOption initialization
	# code to execute.
	autodiscover()