from django.db import models

from world.models import Country

TYPE_CHOICES = ((1, 'Awesome'), (2, 'Good'), (3, 'Normal'), (4, 'Bad'))
TYPE_CHOICES2 = ((1, 'Hot'), (2, 'Normal'), (3, 'Cold'))
TYPE_CHOICES3 = ((1, 'Tall'), (2, 'Normal'), (3, 'Short'))


class KitchenSink(models.Model):
    name = models.CharField(max_length=64)
    help_text = models.CharField(max_length=64, help_text="Enter fully qualified name")
    multiple_in_row = models.CharField(max_length=64, help_text='Help text for multiple')
    multiple2 = models.CharField(max_length=10, blank=True)
    textfield = models.TextField(blank=True, verbose_name='Autosized textarea', help_text='Try and enter few some more lines')

    file = models.FileField(upload_to='.', blank=True)
    readonly_field = models.CharField(max_length=127, default='Some value here')

    date = models.DateField(blank=True, null=True)
    date_and_time = models.DateTimeField(blank=True, null=True)

    date_widget = models.DateField(blank=True, null=True)
    datetime_widget = models.DateTimeField(blank=True, null=True)

    boolean = models.BooleanField(default=True)
    boolean_with_help = models.BooleanField(help_text="Boolean field with help text")

    horizontal_choices = models.SmallIntegerField(choices=TYPE_CHOICES, default=1, help_text='Horizontal choices look like this')
    vertical_choices = models.SmallIntegerField(choices=TYPE_CHOICES2, default=2, help_text="Some help on vertical choices")
    choices = models.SmallIntegerField(choices=TYPE_CHOICES3, default=3, help_text="Help text")
    hidden_checkbox = models.BooleanField()
    hidden_choice = models.SmallIntegerField(choices=TYPE_CHOICES3, default=2, blank=True)
    hidden_charfield = models.CharField(max_length=64, blank=True)
    hidden_charfield2 = models.CharField(max_length=64, blank=True)

    country = models.ForeignKey(Country, related_name='foreign_key_country', on_delete=models.CASCADE)
    linked_foreign_key = models.ForeignKey(Country, limit_choices_to={'continent__name': 'Europe'}, related_name='foreign_key_linked', on_delete=models.CASCADE)
    raw_id_field = models.ForeignKey(Country, help_text='Regular raw ID field', null=True, blank=True, on_delete=models.SET_NULL)

    enclosed1 = models.CharField(max_length=64, blank=True)
    enclosed2 = models.CharField(max_length=64, blank=True)

    def __unicode__(self):
        return self.name


# Inline model for KitchenSink
class Fridge(models.Model):
    kitchensink = models.ForeignKey(KitchenSink, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField(choices=TYPE_CHOICES3)
    description = models.TextField(blank=True)
    is_quiet = models.BooleanField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.name


# Inline model for KitchenSink
class Microwave(models.Model):
    kitchensink = models.ForeignKey(KitchenSink, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField(choices=TYPE_CHOICES3, default=2,
                                    help_text='Choose wisely')
    is_compact = models.BooleanField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.name
