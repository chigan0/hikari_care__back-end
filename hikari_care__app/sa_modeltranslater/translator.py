import copy
from typing import Iterable

from django.conf import settings
from django.db.models import Field, base

from .util_model import get_field, SaTransModel
from .dataclasses import SaTranslationField

class FieldsAggregationMetaClass(type):
	"""
	Metaclass to handle custom inheritance of fields between classes.
	"""

	def __new__(cls, name, bases, attrs):
		if not attrs.get('fields', None):
			return super().__new__(cls, name, bases, attrs)

		attrs['fields'] = list(attrs['fields'])
		
		for base in bases:
			if isinstance(base, FieldsAggregationMetaClass):
				base_fields = getattr(base, 'fields', None)
				if base_fields:
					attrs['fields'].extend(base_fields)  # вместо append!

		attrs['fields'] = tuple(attrs['fields'])
		
		return super().__new__(cls, name, bases, attrs)

 
class SaTranslationOptions(metaclass=FieldsAggregationMetaClass):
	pass


class SaTranslation:
	def __init__(self): 
		self._registry = {}

	def register(self, model: base.ModelBase, opts_class=None, **options):
		sa_field: SaTranslationField

		if model in self._registry:
			return  # уже зарегистрировано
		
		self._registry[model] = opts_class
		fields: Iterable[SaTranslationField] = getattr(opts_class, 'fields', [])

		for sa_field in fields:
			field: Field = model._meta.get_field(sa_field.field_name)

			for lang in settings.LANGUAGES:
				lang_code, _ = lang
				translated_field_name = f"{sa_field.field_name}_{lang_code}"

				# если поле уже есть, пропускаем
				if hasattr(model, translated_field_name):
					continue

				# создаём копию поля
				new_field = copy.deepcopy(field)
				new_field.attname = translated_field_name
				new_field.name = translated_field_name

				if sa_field.params and lang_code in sa_field.params:
					for attr, value in sa_field.params[lang_code].dict().items():
						setattr(new_field, attr, value)

				# самое главное — регистрируем в Django ORM:
				model.add_to_class(translated_field_name, new_field)

			# if sa_field.remove_og_attr:
			field.editable = False
			field.null = True
			field.blank = False

				# if hasattr(model, sa_field.field_name):	
				# 	delattr(model, sa_field.field_name)

				# # Перезаписываем local_fields без указанного поля
				# model._meta.local_fields = [
				# 	f for f in model._meta.local_fields if f.name != sa_field.field_name
				# ]

			if SaTransModel not in model.__bases__:
				model.__bases__ = (*model.__bases__, SaTransModel )

			# Monkey patch
			model._meta.get_field = get_field.__get__(model._meta, model._meta.__class__)

sa_translator = SaTranslation()
