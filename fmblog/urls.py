from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from bloges import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bloges.urls', namespace='bloges')),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)