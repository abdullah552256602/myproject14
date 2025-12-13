"""
URL configuration for myproject14 project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ============================
    # روابط التطبيقات الجديدة
    # ============================
    path('', include('core.urls')),              # الصفحة الرئيسية والمحتوى العام
    path('products/', include('products.urls')), # المنتجات
    path('orders/', include('orders.urls')),     # السلة والطلبات
]
