from django.contrib import admin
from main.models import BrokerRequest

class BrokerRequestAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'mobile_number', 'expected_transaction_amounts_per_month', 
                    'region', 'years_of_experience', 'created_at', 'updated_at', )
    
    # Fields to make searchable
    search_fields = ('name', 'mobile_number', 'region')
    
    # Filters to use in the right sidebar
    list_filter = ('region', 'years_of_experience', 'created_at', 'updated_at')
    
    # Readonly fields (audit fields should not be editable directly)
    readonly_fields = ('created_at', 'updated_at', )
    
    # Fields to display in the detail view
    fieldsets = (
        (None, {
            'fields': ('name', 'mobile_number', 'expected_transaction_amounts_per_month', 
                       'region', 'years_of_experience')
        }),
        ('Audit Information', {
            'fields': ('created_at', 'updated_at', )
        }),
    )
    
    # Automatically set created_by and updated_by
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

# Register the Broker model with the customized admin
admin.site.register(BrokerRequest, BrokerRequestAdmin)
