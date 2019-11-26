from django.contrib import admin
from .models import Register


class Regadmin(admin.ModelAdmin):
    list_display = ('name', 'mobno', 'email', 'uname', 'pwd', 'cpwd')

    class meta:
        model = Register


admin.site.register(Register, Regadmin)
