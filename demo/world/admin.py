from django.contrib import admin

from world.models import City


class CityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'country__name')
    list_display = ('name', 'country', 'capital', 'continent')
    list_filter = ('capital',)
    list_per_page = 5
    fieldsets = [
        (None, {'fields': ['name', 'country', 'capital']}),
        ('Statistics', {
            'description': 'EnclosedInput widget examples',
            'fields': ['area', 'population']}),
    ]

    def continent(self, obj):
        return obj.country.continent


admin.site.register(City, CityAdmin)
