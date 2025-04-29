from datetime import datetime, date
from typing import Any, Dict, List, Optional, Union, Callable, Iterable, Generator, Tuple

from django.db import models
from django.utils.translation import get_language, activate
from django.conf import settings
from django.db.models.options import Options as DjangoOptions

def get_field(self, field_name):
	try:
		return type(self).get_field(self, field_name)
	
	except Exception:
		localized_name = f"{field_name}_{get_language()}"
		try:
			return type(self).get_field(self, localized_name)
		except Exception:
			raise

class SaTransModel:
	LANGS_LIST: List[str] = [lang[0] for lang in settings.LANGUAGES]
	
	def __getattribute__(self, attr_name: str) -> Any:
		try:
			# доступ к __dict__ напрямую, чтобы избежать рекурсии
			obj_dict = super().__getattribute__('__dict__')
			localized_name = f"{attr_name}_{get_language()}"
			
			if localized_name in obj_dict:
				return obj_dict[localized_name]

			# если локализованный не найден — ищем оригинальный атрибут
			return super().__getattribute__(attr_name)

		except AttributeError:
			# если ничего не найдено — кидаем ошибку
			raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr_name}'")
		
	def set_lang_value(self, attr_name: str, value: Any) -> None:
		setattr(self, f"{attr_name}_{get_language()}", value)
		
	def lang_callback(self, callback: callable, *args, **kwargs):
		og_lang: str = get_language()

		for lang, _ in settings.LANGUAGES:
			activate(lang)
			callback(*args, **kwargs)

		activate(og_lang)
		# ac


class SaUtilModel:
	@classmethod
	def get_or_none(cls, **kwargs: dict) -> Optional[models.Model]:
		# Извлекаем параметры для методов запроса
		query_methods = kwargs.pop('query_methods', {})
		
		# Начинаем с базового запроса
		query = cls.objects
		
		# Применяем каждый метод из query_methods
		for method_name, method_args in query_methods.items():
			if isinstance(method_args, dict):
				# Для методов, принимающих именованные аргументы (например, filter)
				query = getattr(query, method_name)(**method_args)
			elif isinstance(method_args, (list, tuple)):
				# Для методов, принимающих позиционные аргументы (например, select_related)
				query = getattr(query, method_name)(*method_args)
			else:
				# Для методов без аргументов
				query = getattr(query, method_name)()

		try:
			# Выполняем запрос с остальными фильтрами
			return query.get(**kwargs)
		
		except cls.DoesNotExist:
			return None

	def __get_lang_in_attr(self, attr: str, lang_delimiter: str) -> Optional[Tuple[str, str]]:
		words: List[str] = attr.split(lang_delimiter)
		return (words[0], words[-1]) if len(words) <= 2 else (lang_delimiter.join(words[0:-1]), words[-1])

	def __model_fields(
		self,
		lang_delimiter: str,
		only_fields: Iterable[str] | None = None, 
		exclude_none: bool = True, 
		exclude_keys: List[str] = [],
		exclude_relations: bool = True
	) -> Generator[Tuple[str, Any], None, None]:
		for field in self._meta.fields:
			field_name: str = field.name
			field_value: Any = getattr(self, field.name)

			if any(lang in field.name for lang in self.LANGS_LIST):
				field_name, lang = self.__get_lang_in_attr(field_name, lang_delimiter)
				
				if get_language() != lang:
					continue
				
				field_value = getattr(self, field_name)

			if exclude_relations and field.is_relation:
				continue

			# Исключение полей с None, если это требуется
			if exclude_none and type(field_value) != bool and not field_value:
				continue

			# Исключение полей по ключам
			if field.name in exclude_keys:
				continue

			# Включаем только указанные поля, если они заданы
			if only_fields and field_name not in only_fields:
				continue

			# Возвращаем имя поля и его значение
			yield field_name, field_value

	def _filter_dict(
		self,
		lang_delimiter: str,
		call_to_key: Dict[str, Dict[str, List[Union[str, Callable]]]],
		only_fields: List[str] | None = None,
		exclude_none: bool = True,  
		exclude_keys: List[str] = [],  
		rename_keys: Dict[str, str] | None = None,  
		auto_convert_datetime: bool = True,
		datetime_format: str = None,
		exclude_relations: bool = True
	) -> Dict[str, Any]:
		filtered_dict: Dict[str, Any] = {}
		model_field = self.__model_fields(
			lang_delimiter, 
			only_fields, 
			exclude_none, 
			exclude_keys, 
			exclude_relations
		)
		
		for db_key, value in model_field:
			attr_key: str = db_key

			if attr_key in call_to_key and value:
				key_obj: models.Model = getattr(self, attr_key)
				for key_type, key_values in call_to_key[attr_key].items():
					
					if key_type == 'attrs':
						for attr in key_values:
							value = getattr(key_obj, attr)
					
					elif key_type == 'methods':
						for method in key_values:
							value = method(value)

			if auto_convert_datetime and isinstance(value, (datetime, date)):
				value = value.strftime(datetime_format)

			filtered_dict[attr_key] = value

		# Переименование ключей
		if rename_keys:
			filtered_dict = {
				rename_keys.get(key, key): value for key, value in filtered_dict.items()
			}

		return filtered_dict

	def get_json(  
		self,
		exclude_keys: List[str] = [],
		additi_keys_pre: Dict[Any, Any] = {},
		additi_keys_lst: Dict[Any, Any] = {},
		call_to_key: Dict[str, Dict[str, List[Union[str, Callable]]]] = {},
		only_fields: Optional[List[str]] = None,
		lang_delimiter: str = '_',
		rename_keys: Optional[Dict[str, str]] = None,  
		exclude_none: bool = True,
		auto_convert_datetime: bool = True,
		datetime_format: str = "%d.%m.%Y",
		exclude_relations: bool = True
	) -> Dict[str, Any]:
		filtered_dict: Dict[str, Any] = self._filter_dict(
			lang_delimiter,
			call_to_key,
			only_fields,
			exclude_none,  
			exclude_keys,  
			rename_keys,
			auto_convert_datetime,
			datetime_format,
			exclude_relations
		)

		return {**additi_keys_pre, **filtered_dict, **additi_keys_lst}
