from django.contrib import admin
from .models import Lead



# ===============================
# IDs Admin Table Display
# ===============================
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'phone', 'status')
    list_display_links = ('id', 'first_name')
    list_editable = ('status',)
    list_per_page = 15


admin.site.register(Lead, LeadAdmin)