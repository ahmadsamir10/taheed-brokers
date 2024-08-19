from django.db import models

class SiteSettings(models.Model):
    banner_content = models.TextField(null=True, blank=True)  # Content for the banner
    display_banner = models.BooleanField(default=True)  # Toggle to display the banner
    stop_renting = models.BooleanField(default=False)  # Toggle to stop renting
    company_bank_details = models.TextField(null=True, blank=True)  # Company bank account details

    def __str__(self):
        return "Site Settings"


from django.db import models

class TermsAndConditions(models.Model):
    title = models.CharField(max_length=512, verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "الشروط والأحكام"
        verbose_name_plural = "الشروط والأحكام"

    def __str__(self):
        return self.title


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=512, verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "سياسة الخصوصية"
        verbose_name_plural = "سياسات الخصوصية"

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=512, verbose_name="السؤال")
    answer = models.TextField(verbose_name="الإجابة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "السؤال الشائع"
        verbose_name_plural = "الأسئلة الشائعة"

    def __str__(self):
        return self.question
