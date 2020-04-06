from django.contrib import admin

# Inlines for KitchenSink
from sample.models import Fridge, Microwave, KitchenSink
from world.models import Country, Continent, City


class CountryInline(admin.StackedInline):
    model = Country
    fields = ('name', 'code', 'population',)
    extra = 1
    verbose_name_plural = 'Countries'


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'countries')
    inlines = (CountryInline,)

    def countries(self, obj):
        return len(obj.country_set.all())


class CityInline(admin.TabularInline):
    model = City
    extra = 3
    verbose_name_plural = 'Cities'
    suit_classes = 'suit-tab suit-tab-cities'


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
    list_display = ('name', 'code', 'continent', 'independence_day')
    list_filter = ('continent',)
    date_hierarchy = 'independence_day'
    list_select_related = True

    inlines = (CityInline,)

    fieldsets = [
        (None, {
            'fields': ['name', 'continent', 'code', 'independence_day']
        }),
        ('Statistics', {
            'fields': ['area', 'population']}),
        ('Textarea', {
            'description': 'Textarea widget example',
            'fields': ['description']}),
        ('Architecture', {
            'fields': ['architecture']}),
    ]


class FridgeInline(admin.TabularInline):
    model = Fridge
    extra = 1
    verbose_name_plural = 'Fridges (Tabular inline)'


class MicrowaveInline(admin.StackedInline):
    model = Microwave
    extra = 1
    verbose_name_plural = 'Microwaves (Stacked inline)'


@admin.register(KitchenSink)
class KitchenSinkAdmin(admin.ModelAdmin):
    inlines = (FridgeInline, MicrowaveInline)
    search_fields = ['name']
    radio_fields = {"horizontal_choices": admin.HORIZONTAL,
        'vertical_choices': admin.VERTICAL}
    list_editable = ('boolean',)
    list_filter = ('choices', 'date')
    readonly_fields = ('readonly_field',)
    raw_id_fields = ('raw_id_field',)
    fieldsets = [
        (None, {'fields': ['name', 'help_text', 'textfield',
            ('multiple_in_row', 'multiple2'),
            'file', 'readonly_field']}),
        ('Date and time', {
            'fields': ['date_widget', 'datetime_widget']}),

        ('Foreign key relations',
        {'description': 'Original select and linked select feature',
            'fields': ['country', 'linked_foreign_key', 'raw_id_field']}),

        ('EnclosedInput widget',
        {
            'fields': ['enclosed1', 'enclosed2']}),

        ('Boolean and choices',
        {'fields': ['boolean', 'boolean_with_help', 'choices',
            'horizontal_choices', 'vertical_choices']}),

        ('Collapsed settings', {
            'classes': ('collapse',),
            'fields': ['hidden_checkbox', 'hidden_choice']}),
        ('And one more collapsable', {
            'classes': ('collapse',),
            'fields': ['hidden_charfield', 'hidden_charfield2']}),

    ]
    list_display = (
        'name', 'help_text', 'choices', 'horizontal_choices', 'boolean')

    def get_formsets(self, request, obj=None):
        """
        Set extra=0 for inlines if object already exists
        """
        for inline in self.get_inline_instances(request):
            formset = inline.get_formset(request, obj)
            if obj:
                formset.extra = 0
            yield formset
