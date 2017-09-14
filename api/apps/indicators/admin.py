from django.contrib import admin

from apps.indicators.models import UF


class UFAdmin(admin.ModelAdmin):
    queryset = UF.objects.all()
    list_display = ('id', 'date', 'value', 'created_ts',)


admin.site.register(UF, UFAdmin)
