from typing import Iterable

from django.db.models.base import ModelBase
from django.db.models import Field
from django.conf import settings

# Лень сортировать языковые поля, это помогает в этом 
def sa_trans_fields(model: ModelBase, trans_fields: Iterable) -> dict[str, list[str]]:
	field: Field
	fields = { lang[0]: [] for lang in settings.LANGUAGES}

	def add_to_fields(field_name: str) -> None:
		for lang in settings.LANGUAGES:
			fields[lang[0]].append( f"{field_name}_{lang[0]}" )

	for field in model._meta.fields:
		if field.name in trans_fields:
			add_to_fields(field.name)

	return fields