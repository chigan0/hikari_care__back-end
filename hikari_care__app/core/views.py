from http import HTTPStatus

from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, response

from .models import MINDType, MIND, PriceList
from .serializers import MINDSerializer, PriceListSerializer
from .filters import PriceListFilter

class MINDListView(generics.ListAPIView):
	serializer_class = MINDSerializer
	filter_backends = ( DjangoFilterBackend, )
	filterset_fields = ("clinic_type", )
		
	def get_queryset(self):
		return MIND.objects.select_related('icon')
	
	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)

		return response.Response({
			"MINDType": { m_type.UUID: m_type.name for m_type in MINDType.objects.all() },
			"MIND": serializer.data,			
		})


class PriceListView(generics.ListAPIView):
	queryset = PriceList.objects.all()
	serializer_class = PriceListSerializer
	filter_backends = (DjangoFilterBackend,)
	filterset_class = PriceListFilter
	#filterset_fields = PriceListFilter

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)
		grouped = {}
		
		for item in serializer.data:
			mind = item.pop('mind')  # достаем mind и убираем из item
			
			if mind["id"] not in grouped:
				grouped[mind["id"]] = {
					"MINDName": mind["name"],
					"items": []
				}
			
			grouped[mind["id"]]["items"].append({
				"name": item["name"],
				"priceInKzt": item["price_in_kzt"],
				"procedure": item["procedure"]
			})

		return response.Response(grouped)