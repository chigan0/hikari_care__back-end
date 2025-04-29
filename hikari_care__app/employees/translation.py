from typing import Iterable

from sa_modeltranslater import register, SaTranslationOptions, SaTranslationField, SaTranslationFieldParams
from .models import Employee

@register(Employee)
class EmployeeTranslationOptions(SaTranslationOptions):
	fields = [
		SaTranslationField(field_name="qualification"),
		SaTranslationField(field_name="job_title"),
		SaTranslationField(field_name="about_employee"),
		SaTranslationField(field_name="last_name"),
		SaTranslationField(field_name="first_name"),
		SaTranslationField(field_name="middle_name"),
	]