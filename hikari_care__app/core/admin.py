from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import MINDType, MIND, Procedure, PriceList
from sa_gallery.admin_base import SaGalleryImageAdmin
from utils import sa_trans_fields

@admin.register(MINDType)
class MINDTypeAdmin(admin.ModelAdmin):
	list_display = ("name", "created_at", "updated_at")


@admin.register(MIND)
class MINDAdmin(admin.ModelAdmin):
	list_display = ("name", "created_at", "updated_at")
	trans_fields = sa_trans_fields(MIND, ("name", "desc", ))

	fieldsets = (
		( _("На русском"), {"fields": trans_fields["ru"]} ),
		( _("На казахском"), {"fields": trans_fields["kk"]} ),
		( _("На англиском"), {"fields": trans_fields["en"]} ),
		( _("Дополнительнная информация") , { "fields": ("clinic_type", "icon") } )
	)


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
	list_display = ( "name", "created_at", "updated_at" )
 

@admin.register(PriceList)
class PriceListAdmiin(admin.ModelAdmin):
	search_fields = ("name_kk", "name_ru", "name_en")
	list_display = ( "name", "mind", "procedure", "price_in_kzt" )
