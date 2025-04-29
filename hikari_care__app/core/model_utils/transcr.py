from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Iterable

from .text_styles import *

class TranscrStyleNotFound(ValueError):
	pass


class Transcr:
	transcr_rules: Dict[str, Dict[str, str]] = {}
	transcr_rules_example: Dict[str, Dict[str, str]] = {
		# Стандартная транскрипция букв
		"а": {"default": "a"},
		"е": {"default": "e", "start": "ye"},  # "е" в начале слова → "ye"
		"и": {"default": "i"},
		"о": {"default": "o"},
		"у": {"default": "u"},
		"ы": {"default": "y"},
		"э": {"default": "e"},
		"б": {"default": "b"},
		"в": {"default": "v"},
		"г": {"default": "g"},
		"д": {"default": "d"},
		"ж": {"default": "zh"},
		"з": {"default": "z"},
		"к": {"default": "k"},
		"л": {"default": "l"},
		"м": {"default": "m"},
		"н": {"default": "n"},
		"п": {"default": "p"},
		"р": {"default": "r"},
		"с": {"default": "s"},
		"т": {"default": "t"},
		"ф": {"default": "f"},
		"ч": {"default": "ch"},
		"ш": {"default": "sh"},
		"щ": {"default": "shch"},
		"ц": {"default": "ts"},
		"й": {"default": "y"},
		"х": {"default": "kh"},
		"ю": {"default": "yu", "start": "yu"},
		"я": {"default": "ya", "start": "ya"},
		"ё": {"default": "yo", "start": "yo"},
		"ъ": {"default": ""},  # Твёрдый знак пропускается
		"ь": {"default": "'"}   # Мягкий знак передаётся апострофом
	}

	def __init__(self):
		# Создание правил для заглавных букв
		for symb, rules in self.transcr_rules_example.items():
			self.transcr_rules[symb] = rules
			self.transcr_rules[symb.upper()] = {key: value.upper() for key, value in rules.items()}

	def _word_processor(self, word: str, ignore_symbols: list) -> str:
		transcr_word = ""
		for i, symb in enumerate(word):
			# Игнорируем мусорные символы
			if symb in ignore_symbols:
				continue

			# Определяем позицию символа в слове
			if i == 0:
				pos = "start"
			elif i == len(word) - 1:
				pos = "end"
			else:
				pos = "middle"
			
			# Применяем транскрипционные правила
			symb_transcr = self.transcr_rules.get(symb, {}).get(pos, self.transcr_rules.get(symb, {}).get("default", symb))
			transcr_word += symb_transcr

		return transcr_word

	def convert_txt_to_style(self, text: Iterable[str], style: TextStyleInterface) -> str:
		word: str = style.join_symb.join(text)
		text_transform: Optional[str] = style.text_transform

		if text_transform:
			word = getattr(word, text_transform)()

		return word

	def processing(self, words: str, text_style: TextStyleInterface = KebabCaseStyle(), word_split: str = ' ') -> str:
		processed_words: List[str] = []
		words_list: List[str] = words.strip().split(word_split)
		ignore_symbols = text_style.ignore_symbols
		
		for word in words_list:
			word_transcr = self._word_processor(word, ignore_symbols)
			if word_transcr:
				processed_words.append(word_transcr)
		
		return self.convert_txt_to_style(processed_words, text_style)

