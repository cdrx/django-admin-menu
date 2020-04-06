from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_custom_logo():
    return getattr(settings, 'ADMIN_LOGO', None)
