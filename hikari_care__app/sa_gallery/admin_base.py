from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import SaGalleryImage

def view_image(image, width: str = '150px', height: str = '80px', style: str = "object-fit: cover"):
	if image:
		return format_html(
			'''
				<a href="{}" target="_blank">
					<img src="{}" width="{}" height="{}" style="{}" />
				</a>
			''',
			image.url, image.url, width, height, style
		)
	
	return _('No image')


@admin.register(SaGalleryImage)
class SaGalleryImageAdmin(admin.ModelAdmin):
	search_fields = ("title", "original")
	# image_format
	list_display = ("title", "original", "created_at", "preview")

	# fieldsets = (
	# 	(_('Base'), {
	# 		'fields': ('name', 'image')
	# 	}),

	# 	(_('Compression'), {
	# 		'fields': ('compression_status', 'width', 'height', 'quality', 'image_format')
	# 	}),
	# )

	preview = lambda _, obj: view_image(obj.original)
	preview.short_description = _('Background image')

