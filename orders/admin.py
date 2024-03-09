from django.contrib import admin
from . models import OrderedItem,Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter =[
        "owner",
        "order_status",
    ]
    search_fields = (
        "owner",
        "id",
    )

admin.site.register(Order, OrderAdmin)