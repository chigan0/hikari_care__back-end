from tinymce.models import HTMLField
from django.db import models
from django.utils.translation import get_language, gettext_lazy as _
from bs4 import BeautifulSoup

from core.abstract_models import TimeStampedModel, AutoSeoTeg

class News(TimeStampedModel, AutoSeoTeg):
	title = models.CharField(max_length=256, unique=True, null=False, blank=False, verbose_name=_("Заголовок"))
	desc = HTMLField(blank=True, null=True, verbose_name=_("Новость"))
	small_desc = models.TextField(blank=True, null=True, verbose_name=_("Краткий подзаголовок новости"))

	title_image = models.ForeignKey(
		"sa_gallery.SaGalleryImage",
		blank=True,
		on_delete=models.CASCADE,
		verbose_name=_("Главное изображение"),
		help_text=_('Search occurs by internal name or by image name'),
		null=True
	)

	created_at_ed = models.DateField(verbose_name=_("Дата создания"))

	def __str__(self) -> str:
		return f"{self.title}"
	
	def auto_small_desc(self, max_word_count: int = 15) -> str:
		if self.small_desc or not self.desc:
			return None
		
		text = BeautifulSoup(self.desc, "html.parser").get_text()
		self.set_lang_value("small_desc", " ".join(text.split()[:max_word_count]))

	def save(self, *args, **kwargs):
		self.lang_callback(self.auto_small_desc)
		self.set_seo_name(self.title_ru)
		super().save(*args, **kwargs)

	class Meta(TimeStampedModel.Meta, AutoSeoTeg.Meta):
		verbose_name = _("Новость")
		verbose_name_plural = _("Новости")
		ordering = ["-created_at_ed", "-id"]