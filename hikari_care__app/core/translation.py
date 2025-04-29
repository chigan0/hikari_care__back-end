from django.utils.translation import get_language, gettext_lazy as _

from sa_modeltranslater import register, SaTranslationOptions, SaTranslationField, SaTranslationFieldParams
from .models import MIND, Procedure, PriceList, MINDType

@register(MINDType)
class MINDTypeTranslationOptions(SaTranslationOptions):
	fields = [
		SaTranslationField(
			field_name="name",
			params={
				"ru": SaTranslationFieldParams(verbose_name="Заголовок ( на русском )"),
				"kk": SaTranslationFieldParams(verbose_name="Заголовок ( на казахском )"),
				"en": SaTranslationFieldParams(verbose_name="Заголовок ( на англиском )",)
			}
		)
	]


@register(MIND)
class MINDTranslationOptions(SaTranslationOptions):
	fields = [
		SaTranslationField(field_name="desc"),
		SaTranslationField(field_name="name")
	]


@register(Procedure)
class ProcedureTranslationOptions(SaTranslationOptions):
	fields = [
		SaTranslationField(
			field_name="name",
			params={
				"ru": SaTranslationFieldParams(verbose_name=_("Procedure (in Russian)")),
				"kk": SaTranslationFieldParams(verbose_name=_("Procedure (in Kazakh)")),
				"en": SaTranslationFieldParams(verbose_name=_("Procedure (in English)"))
			}
		)
	]


@register(PriceList)
class PriceListTranslationOptions(SaTranslationOptions):
	fields = [ 
		SaTranslationField(
			field_name="name",
			params={
				"ru": SaTranslationFieldParams(verbose_name=_("Procedure names (in Russian)")),
				"kk": SaTranslationFieldParams(verbose_name=_("Procedure names (in Kazakh)")),
				"en": SaTranslationFieldParams(verbose_name=_("Procedure names (in English)"))
			}
		),
	 ]
