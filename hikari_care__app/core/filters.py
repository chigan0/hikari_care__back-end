from django_filters import rest_framework as filters

from .models import PriceList

class PriceListFilter(filters.FilterSet):
	uuid = filters.UUIDFilter(field_name="mind__uuid") 

	class Meta:
		model = PriceList
		fields = ['uuid']
