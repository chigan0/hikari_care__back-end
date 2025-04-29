from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Employee
from utils import sa_trans_fields

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	# filter_horizontal = ('mind',)
	search_fields = ("last_name_ru", "first_name_ru", "middle_name_ru")
	list_display = ("last_name", "job_title", "created_at", "updated_at")

	trans_fields = sa_trans_fields(
		Employee, 
		(
			"qualification", 
			"job_title", 
			"about_employee", 
			"last_name", 
			"first_name", 
			"middle_name"
		),
	)

	fieldsets = (
		( _("На русском"), {"fields": trans_fields["ru"]} ),
		( _("На казахском"), {"fields": trans_fields["kk"]} ),
		( _("На англиском"), {"fields": trans_fields["en"]} ),
		( _("Дополнительнная информация") , { "fields": ("med_total_exp", "exp_in_the", "photo", "mind") } )
	)
