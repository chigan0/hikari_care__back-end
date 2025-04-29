from django.db import models
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from .validators import ImageAndSvg

class SaGalleryImage(models.Model):
	title = models.CharField(max_length=256, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	original = models.ImageField(
		upload_to="gallery/originals/", 
		verbose_name=_("Image link"), 
		validators=[ImageAndSvg.validate]
	)

	def __str__(self) -> str:
		return f"{self.title if self.title else self.original.file.name.split('/')[-1]}"
	
	def get_image_url(self, request: HttpRequest):
		return request.build_absolute_uri(self.image.url)

	class Meta:
		verbose_name = _("Image")
		verbose_name_plural = _("Gallery")
