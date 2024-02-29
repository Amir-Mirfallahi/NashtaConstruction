from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

