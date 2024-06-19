from django.contrib import admin
from .models import chaiVariety, ChaiReview, Store, chaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class chaiCertificateInline(admin.StackedInline):
    model = chaiCertificate
    extra = 1
    
class chaiVarietyAdmin(admin.ModelAdmin):
    inlines = [ChaiReviewInline, chaiCertificateInline]
    list_display = ('name', 'type', 'price')
    search_fields = ['name', 'type']
    list_filter = ['type']

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)

admin.site.register(chaiVariety, chaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)  