from sa_modeltranslater import register, SaTranslationOptions, SaTranslationField
from .models import News

@register(News)
class NewsTranslationOptions(SaTranslationOptions):
	fields = [
		SaTranslationField(field_name="title"),
		SaTranslationField(field_name="desc"),
		SaTranslationField(field_name="small_desc")
	]
