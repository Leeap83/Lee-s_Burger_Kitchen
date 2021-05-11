from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_id', 'created_on',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_id', 'created_on', 'name',
              'email', 'phone_number', 'street',
              'town_or_city', 'postcode', 'county',
              'delivery_cost', 'order_total',
              'grand_total', 'order_status', 'original_cart',
              'stripe_pid')

    list_display = ('order_id', 'created_on', 'name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-created_on',)


admin.site.register(Order, OrderAdmin)
