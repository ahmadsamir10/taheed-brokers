from django.db import models

class BrokerRequest(models.Model):
    name = models.CharField("الاسم", max_length=255)
    mobile_number = models.CharField("رقم الجوال", max_length=15, unique=True)
    expected_transaction_amounts_per_month = models.DecimalField("المبالغ المتوقعة للمعاملات شهريًا", max_digits=10, decimal_places=2)
    region = models.CharField("المنطقة", max_length=255)
    years_of_experience = models.PositiveIntegerField("سنوات الخبرة")
    # audit logs
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)

    def __str__(self):
        return self.name
