from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from jum.views.main import MainView, custom_handler404, custom_handler500

urlpatterns = [
    path('login/', include('login.urls')),
    path('jum/', include('jum.urls')),
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_handler404
handler500 = custom_handler500
