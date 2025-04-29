from rest_framework import generics

from .models import News
from .serializers import NewsSerializer

class NewsSerializerListView(generics.ListAPIView):
	serializer_class = NewsSerializer

	def get_queryset(self):
		return News.objects.select_related('title_image')

	def get_serializer_context(self):
		context = super().get_serializer_context()
		context["exclude_desc"] = True 
		return context


class NewsDetailView(generics.RetrieveAPIView):
	serializer_class = NewsSerializer
	lookup_field = "seo_name"
	# filter_backends = ( DjangoFilterBackend, )
	# filterset_fields = ("mind", )

	def get_queryset(self):
		return News.objects.select_related('title_image')
