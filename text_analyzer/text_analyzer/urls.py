from django.contrib import admin
from django.urls import path, include
from analyzer.views import upload_file
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Text Analyzer API",
      default_version='v1',
      description="Документация для API анализа текста",
      terms_of_service="https://your-terms-url.com",
      contact=openapi.Contact(email="support@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# Основные URL-шаблоны проекта
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),  # ← оставить
    # path("api/", include("analyzer.urls")),  ← УДАЛИТЬ или переместить

    path('analyzer/', include('analyzer.urls')),  # ← если analyzer нужен — пусть будет отдельно
    path('', upload_file, name='upload'),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]


# Добавление обработки медиафайлов в режиме разработки
# static() работает ТОЛЬКО при DEBUG=True
# В production нужно настраивать через веб-сервер (Nginx/Apache)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)