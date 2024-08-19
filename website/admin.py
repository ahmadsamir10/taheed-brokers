from django.contrib import admin

class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    # To display Arabic labels in the admin form
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question',)
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
