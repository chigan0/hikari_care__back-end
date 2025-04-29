import uuid

from django.db import models
from django.http import HttpRequest
from django.utils.translation import get_language, gettext_lazy as _
from tinymce.models import HTMLField

from sa_gallery import image_url_or
from sa_modeltranslater import SaUtilModel
from .abstract_models import TimeStampedModel, UUIDModel

class MINDType(TimeStampedModel, UUIDModel):
	name = models.CharField(max_length=128, unique=True, blank=False, null=False, verbose_name=_("Заголовок"))

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = _("Тип мед. учреждения")
		verbose_name_plural = _("Типы мед. учреждений")


class MIND(TimeStampedModel, SaUtilModel, UUIDModel):
	name = models.CharField(max_length=256, unique=True, blank=False, verbose_name=_("Заголовок"))
	clinic_type = models.ManyToManyField(MINDType, verbose_name=_("Тип мед. учреждения"))
	icon = models.ForeignKey(
		"sa_gallery.SaGalleryImage", 
		blank=True, 
		on_delete=models.CASCADE, 
		verbose_name=_("Иконка"), 
		help_text=_('Search occurs by internal name or by image name'),
		null=True
	)
	desc = HTMLField(blank=True, null=True, verbose_name=_("Описание услуги"))

	def __str__(self):
		return self.name
	
	def get_json(self, request: HttpRequest):
		return {
			"id": self.id,
			"name": self.name,
			"icon": image_url_or(request, self.icon),
			"MINDType": ( c_type.name for c_type in self.clinic_type.all() )
		}
	
	class Meta:
		verbose_name = _("направление")
		verbose_name_plural = _("направления")


class Procedure(TimeStampedModel):
	name = models.CharField(max_length=256, verbose_name=_("Процедура"))

	def __str__(self) -> str:
		return self.name
	
	class Meta:
		verbose_name = _("Процедура")
		verbose_name_plural = _("Процедуры")


class PriceList(TimeStampedModel):
	name = models.CharField(max_length=256, verbose_name=_("Названия процедуры"), null=True)
	price_in_kzt = models.IntegerField(verbose_name=_("Цена в KZT"))
	mind = models.ForeignKey(MIND, verbose_name=_("направление"), on_delete=models.CASCADE)
	procedure = models.ForeignKey(Procedure, null=False, blank=False, verbose_name=_("Процедура"), on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.name

	class Meta:
		verbose_name = _("Элемент прейскуранта")
		verbose_name_plural = _("Прейскурант")
