from django.urls import path, include
from rest_framework import routers

from .views import MINDListView, PriceListView

# router = routers.DefaultRouter()
# router.register(r"price-list", PriceListViewSet)

urlpatterns = [
	# path( "", include(router.urls) ),
	path( "mind/", MINDListView.as_view()),
	path("price-list/", PriceListView.as_view())
]
