from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sa_gallery.admin_base import SaGalleryImageAdmin
from utils import sa_trans_fields
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	search_fields = ("title_ru", "title_kk", "title_en")
	list_display = ("title", "created_at_ed")
	trans_fields = sa_trans_fields(News, ("title", "desc", "small_desc"))

	fieldsets = (
		( _("На русском"), {"fields": trans_fields["ru"]} ),
		( _("На казахском"), {"fields": trans_fields["kk"]} ),
		( _("На англиском"), {"fields": trans_fields["en"]} ),
		( _("Дополнительнная информация") , { "fields": ("title_image", "created_at_ed") } )
	)
