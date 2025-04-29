from django_filters import rest_framework as filters

from .models import Employee

class EmployeeListFilter(filters.FilterSet):
	uuid = filters.UUIDFilter(field_name="mind__uuid") 

	class Meta:
		model = Employee
		fields = ['uuid']
