from django.db import models

from tinymce.models import HTMLField
from django.utils.translation import get_language, gettext_lazy as _

from core.abstract_models import TimeStampedModel, UUIDModel

class Employee(TimeStampedModel, UUIDModel):
	last_name = models.CharField(max_length=72, blank=False, verbose_name=_("Фамилия"))
	first_name = models.CharField(max_length=72, blank=False, verbose_name=_("Имя"))
	middle_name = models.CharField(max_length=72, null=True, blank=True, verbose_name=_("Отчество"))

	qualification = models.TextField(blank=False, verbose_name=_("Квалификация"))

	med_total_exp = models.IntegerField(blank=False, verbose_name=_("Общий стаж в медицине"))
	exp_in_the = models.IntegerField(blank=False, verbose_name=_("На нынешнем месте работы с какого года"))

	job_title = models.CharField(max_length=256, verbose_name=_("Должность"))
	about_employee = HTMLField(blank=True, null=True, verbose_name=_("О Враче"))
	photo = models.ForeignKey(
		"sa_gallery.SaGalleryImage",
		blank=True,
		on_delete=models.CASCADE,
		verbose_name=_("Фото"),
		help_text=_('Search occurs by internal name or by image name'),
		null=True
	)

	mind = models.ManyToManyField("core.MIND", verbose_name=_("направление"), blank=True)

	def __str__(self) -> str:
		return f"{self.last_name} {self.first_name} {self.middle_name}"

	class Meta(TimeStampedModel.Meta):
		verbose_name = _("Врачь")
		verbose_name_plural = _("Врачи")
