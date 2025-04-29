import os
from typing import List, Optional

from PIL import Image
from django.core.exceptions import ValidationError

# Validators Funcs

def check_valid_extensions(ext: str, valid_extensions: List[str], error_msg: Optional[str] = None):
	if not error_msg:
		error_msg = f"Недопустимый тип файла: {ext}. Разрешенные расширения: {', '.join(valid_extensions)}."

	if ext.lower() not in valid_extensions:
		raise ValidationError(error_msg)	


def file_validator(value, valid_extensions: List[str], max_size:int):
	if value.size > max_size:
		raise ValidationError(f"Размер файла не должен превышать {max_size / (1024 * 1024)}MB.")

	check_valid_extensions(os.path.splitext(value.name)[1], valid_extensions)
	

def image_validator(value, valid_extensions: List[str], max_size: int = 10 * 1024 * 1024):  # 10MB):
	if value.size > max_size:
		raise ValidationError(f"Размер файла не должен превышать {max_size / (1024 * 1024)}MB.")

	check_valid_extensions(os.path.splitext(value.name)[1], valid_extensions)

	try:
		img = Image.open(value)
		img.verify()
	
	except Exception as e:
		raise ValidationError("Загруженный файл не является допустимым изображением.")
	
def video_validator(value, valid_extensions: List[str], max_size: int = 100 * 1024 * 1024):  # 100MB by default
	if value.size > max_size:
		raise ValidationError(f"Размер файла не должен превышать {max_size / (1024 * 1024)}MB.")

	check_valid_extensions(os.path.splitext(value.name)[1], valid_extensions)

# Validators

class FileValidator:
	max_size = 50 * 1024 * 1024  # 5MB
	valid_extensions = ['.pdf', '.doc', '.docx', '.txt', '.svg']

	@staticmethod
	def validate(value):
		return file_validator(value, FileValidator.valid_extensions, FileValidator.max_size,)


class ImageValidator:
	valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

	@staticmethod
	def validate(value):
		return image_validator(value, ImageValidator.valid_extensions)


class ImageAndSvg(FileValidator):
	valid_extensions = [*ImageValidator.valid_extensions, '.svg']

	@staticmethod
	def validate(value):
		return file_validator(value, ImageAndSvg.valid_extensions, ImageAndSvg.max_size)
	

