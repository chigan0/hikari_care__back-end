from typing import Dict
from dataclasses import dataclass

@dataclass(frozen=True)
class SaTranslationFieldParams:
	verbose_name: str | None = None
	default: str | None = None
	blank: bool | None = None
	help_text: str | None = None
	max_length: int | None = None
	null: bool | None = None
	unique: bool | None = None

	def dict(self, nullable: bool = False) -> dict:		
		return dict(
			filter(
				lambda item: True if item[-1] != None else False, self.__dict__.items()
				)
			) if not nullable else self.__dict__


@dataclass(frozen=True)
class SaTranslationField:
	field_name: str
	params: Dict[str, SaTranslationFieldParams] | None = None
	# remove_og_attr: bool = True

