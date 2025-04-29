from django.urls import path

from .views import NewsSerializerListView, NewsDetailView
# from rest_framework import routers

# from .views import EmployeeListView

# router = routers.DefaultRouter()
# router.register(r"price-list", PriceListViewSet)

urlpatterns = [
	path("list/", NewsSerializerListView.as_view()),
	path("<slug:seo_name>/", NewsDetailView.as_view())
	# path( "", include(router.urls) ),
	# path( "list/", EmployeeListView.as_view())
]
