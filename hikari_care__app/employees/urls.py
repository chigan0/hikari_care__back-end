from django.urls import path

from .views import EmployeeListView, EmployeeDetailView

urlpatterns = [
	path("list/", EmployeeListView.as_view()),
	path("<uuid:uuid>", EmployeeDetailView.as_view())
]