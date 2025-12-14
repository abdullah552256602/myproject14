from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(
        max_length=200,
        verbose_name='اسم الموقع',
        help_text='اسم المتجر أو الموقع كما سيظهر للزوار'
    )

    site_description = models.TextField(
        verbose_name='وصف الموقع',
        help_text='وصف مختصر عن الموقع أو المتجر',
        blank=True
    )

    site_email = models.EmailField(
        verbose_name='البريد الإلكتروني',
        help_text='البريد الإلكتروني الرسمي للتواصل'
    )

    site_phone = models.CharField(
        max_length=20,
        verbose_name='رقم التواصل',
        help_text='رقم الهاتف أو الواتساب'
    )

    site_address = models.CharField(
        max_length=255,
        verbose_name='عنوان الموقع',
        help_text='العنوان الفعلي أو المدينة',
        blank=True
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='مفعل',
        help_text='تفعيل أو إيقاف إعدادات الموقع'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإنشاء'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='آخر تحديث'
    )

    class Meta:
        verbose_name = 'إعدادات الموقع'
        verbose_name_plural = 'إعدادات الموقع'
        ordering = ['-created_at']

    def __str__(self):
        return self.site_name
