from django.contrib import admin

from product.models import Cart


class Cartadmin(admin.ModelAdmin):
    list_display = ['pid','units','unitprice','tuprice','image']
    list_filter = ['pid']
    class meta:
        model=Cart


admin.site.register(Cart,Cartadmin)

