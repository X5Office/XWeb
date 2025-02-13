from django.contrib import admin
from WGKApi.models import Files, ProductGroup, GKProduct, Barcode, UnitOfMeasureCode

# Register your models here.
admin.site.register(Files)
admin.site.register(ProductGroup)
admin.site.register(GKProduct)
admin.site.register(Barcode)
admin.site.register(UnitOfMeasureCode)