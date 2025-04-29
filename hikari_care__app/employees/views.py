from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer
from .filters import EmployeeListFilter

class EmployeeListView(generics.ListAPIView):
	queryset = Employee.objects.select_related('photo').prefetch_related("mind")
	serializer_class = EmployeeSerializer
	filter_backends = ( DjangoFilterBackend, )
	# filterset_fields = ("mind", )
	filterset_class = EmployeeListFilter

	def get_serializer_context(self):
		context = super().get_serializer_context()
		context["exclude_fields"] = ("qualification", "bio", "mind") 
		return context


class EmployeeDetailView(generics.RetrieveAPIView):
	queryset = Employee.objects.select_related('photo').prefetch_related("mind")
	serializer_class = EmployeeSerializer
	lookup_field = "uuid"
