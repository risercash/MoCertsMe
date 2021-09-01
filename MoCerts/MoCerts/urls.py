from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static # нужно прописать путь статика для отабражения изображении

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('MainApp.urls')),
]

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print(urlpatterns)