from django.contrib import admin
from .models import Category, Product, ProductImage


# =========================
# إدارة التصنيفات
# =========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


# =========================
# صور المنتجات (Inline)
# =========================
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# =========================
# إدارة المنتجات
# =========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "is_active", "created_at")
    list_filter = ("is_active", "category")
    list_editable = ("price", "stock", "is_active")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]
