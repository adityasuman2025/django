from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

#including the include functioanlity to show views of other apps

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

from companies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('stocks/', views.StockList.as_view()),
    path('', include('music.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)