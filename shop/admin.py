from django.contrib import admin
from .models import product, order, OrderUpdate, ContactUs

# Register your models here.
admin.site.register(product),
admin.site.register(order),
admin.site.register(OrderUpdate),
admin.site.register(ContactUs)