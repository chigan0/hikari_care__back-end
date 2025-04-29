from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Iterable

# Интерфейс для текстового стиля
class TextStyleInterface(ABC):
	@property
	@abstractmethod
	def join_symb(self) -> str:
		pass
	
	@property
	@abstractmethod
	def text_transform(self) -> Optional[str]:
		pass

	@property
	@abstractmethod
	def ignore_symbols(self) -> List[str]:
		pass

# Реализация стилей

class KebabCaseStyle(TextStyleInterface):
	@property
	def join_symb(self) -> str:
		return '-'

	@property
	def text_transform(self) -> Optional[str]:
		return 'lower'

	@property
	def ignore_symbols(self) -> List[str]:
		return ['«', '»', ':', '"', '“', '”', ',', '.', '!', '?', '—', '/', '\\', '%']


class SnakeCaseStyle(TextStyleInterface):
	@property
	def join_symb(self) -> str:
		return '_'

	@property
	def text_transform(self) -> Optional[str]:
		return 'lower'

	@property
	def ignore_symbols(self) -> List[str]:
		return ['«', '»', ':', '"', '“', '”', ',', '.', '!', '?', '—']


class UpperSnakeCaseStyle(TextStyleInterface):
	@property
	def join_symb(self) -> str:
		return '_'

	@property
	def text_transform(self) -> Optional[str]:
		return 'upper'

	@property
	def ignore_symbols(self) -> List[str]:
		return ['«', '»', ':', '"', '“', '”', ',', '.', '!', '?', '—']


class TrainCaseStyle(TextStyleInterface):
	@property
	def join_symb(self) -> str:
		return '-'

	@property
	def text_transform(self) -> Optional[str]:
		return 'title'

	@property
	def ignore_symbols(self) -> List[str]:
		return ['«', '»', ':', '"', '“', '”', ',', '.', '!', '?', '—']


class FlatCaseStyle(TextStyleInterface):
	@property
	def join_symb(self) -> str:
		return ''

	@property
	def text_transform(self) -> Optional[str]:
		return 'lower'

	@property
	def ignore_symbols(self) -> List[str]:
		return ['«', '»', ':', '"', '“', '”', ',', '.', '!', '?', '—']
