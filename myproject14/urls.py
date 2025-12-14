"""
URL configuration for myproject14 project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # ============================
    # روابط التطبيقات
    # ============================
    path('', include('core.urls')),               # الصفحة الرئيسية والمحتوى العام
    path('products/', include('products.urls')),  # المنتجات
    path('orders/', include('orders.urls')),      # السلة والطلبات
]


# ============================
# عرض ملفات media أثناء التطوير
# ============================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
