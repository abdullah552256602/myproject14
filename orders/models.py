from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# =========================
# 🛒 سلة التسوق
# =========================
class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='المستخدم'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإنشاء'
    )

    class Meta:
        verbose_name = 'سلة التسوق'
        verbose_name_plural = 'سلال التسوق'

    def __str__(self):
        return f"سلة {self.user.username}"


# =========================
# 📦 عناصر السلة
# =========================
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='سلة التسوق'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='المنتج'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='الكمية'
    )

    class Meta:
        verbose_name = 'عنصر في السلة'
        verbose_name_plural = 'عناصر السلة'

    def __str__(self):
        return f"{self.quantity} × {self.product}"


# =========================
# 🧾 الطلب
# =========================
class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('processing', 'قيد التجهيز'),
        ('completed', 'مكتمل'),
        ('canceled', 'ملغي'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='العميل'
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='إجمالي الطلب'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='حالة الطلب'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ إنشاء الطلب'
    )

    class Meta:
        verbose_name = 'طلب'
        verbose_name_plural = 'الطلبات'
        ordering = ['-created_at']

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"


# =========================
# 🧾 عناصر الطلب
# =========================
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='الطلب'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='المنتج'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='سعر المنتج'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='الكمية'
    )

    class Meta:
        verbose_name = 'عنصر طلب'
        verbose_name_plural = 'عناصر الطلب'

    def __str__(self):
        return f"{self.quantity} × {self.product}"
