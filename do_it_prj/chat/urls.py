from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "excel"

urlpatterns = [
    path("", views.index, name="index"),
    path('<str:room_name>/', views.room, name='room'),
    # path("download/", views.uploadFile, name="uploadFile"),
    # path("download/", views.downloadFile, name="downloadFile"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
