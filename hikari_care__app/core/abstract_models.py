import uuid

from django.db import models
from django.utils.translation import get_language, gettext_lazy as _

from .model_utils import Transcr

class UUIDModel(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

	@property
	def UUID(self):
		return str(self.uuid)

	class Meta:
		abstract = True

class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Дата создания"))
	updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Дата последнего обновления"))

	class Meta:
		abstract = True


class AutoSeoTeg(models.Model):
	seo_name = models.CharField(max_length=428, null=True, verbose_name=_("SEO названия"))

	class Meta:
		abstract = True

	def set_seo_name(self, name: str) -> None:
		transcr: Transcr = Transcr()
		self.seo_name = transcr.processing(name)
