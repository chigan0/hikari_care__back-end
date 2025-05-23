"""
URL configuration for hikari_care__app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.i18n import set_language

urlpatterns = [
    path('set_language/', set_language, name='set_language'),
	path('tinymce/', include('tinymce.urls'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
	path("api/core/", include("core.urls")),
	path("api/employees/", include("employees.urls")),
	path("api/news/", include("news.urls")),
    path('api/api-auth/', include('rest_framework.urls')),
)

# Маршруты для медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
