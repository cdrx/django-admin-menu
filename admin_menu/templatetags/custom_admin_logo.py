from django.conf import settings
from django import template

register = template.Library()


@register.assignment_tag
def get_custom_logo():
    return getattr(settings, 'ADMIN_LOGO', None)
