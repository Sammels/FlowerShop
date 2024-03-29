from django.contrib import admin

from flower_app.models import Store, Bouquet, BouquetCategory, Order, Courier, ConsultationRequest


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ['address', 'phone_number']


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'image', 'compound', 'size_height', 'size_width', 'category']
    raw_id_fields = ['category']
    list_display = ['name', 'price']


@admin.register(BouquetCategory)
class BouquetCategoryAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['bouquet', 'client_name', 'phone_number', 'delivery_address', 'payment_status', 'delivery_time']
    raw_id_fields = ['bouquet']
    list_display = ['client_name', 'phone_number', 'payment_status']


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    fields = ['tg_id', 'order', 'status']
    raw_id_fields = ['order']


@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    readonly_fields = ['date']
    list_display = ['name', 'phone_number', 'date']
    search_fields = ['name', 'phone_number']
    list_filter = ['date']