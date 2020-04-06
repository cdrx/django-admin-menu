import os.path
from collections import OrderedDict

import sass
from django import template
from django.conf import settings

register = template.Library()

_compiled_sass = None


def sass_variable_defaults():
    return (
        ('background', 'white'),
        ('primary-color', '#205280'),
        ('primary-text', '#d6d5d2'),
        ('secondary-color', '#3B75AD'),
        ('secondary-text', 'white'),
        ('tertiary-color', '#F2F9FC'),
        ('tertiary-text', 'black'),
        ('breadcrumb-color', 'whitesmoke'),
        ('breadcrumb-text', 'black'),
        ('focus-color', '#eaeaea'),
        ('focus-text', '#666'),
        ('primary-button', '#26904A'),
        ('primary-button-text', 'white'),
        ('secondary-button', '#999'),
        ('secondary-button-text', 'white'),
        ('link-color', '#333'),
        ('link-color-hover', 'lighten($link-color, 20%)')
    )


def sass_variables():
    variables = OrderedDict(sass_variable_defaults())
    custom = getattr(settings, 'ADMIN_STYLE', {})
    for v, c in custom.items():
        variables[v] = c

    sass = ""
    for v, c in variables.items():
        sass += "$%s: %s;\n" % (
            v, c
        )

    return sass


def get_sass_source():
    src = os.path.join(os.path.dirname(__file__), '..', 'sass', 'admin-menu.scss')
    with open(src) as f:
        sass = f.read()

    variables = sass_variables()

    return "%s\n\n%s" % (
        variables,
        sass
    )


@register.simple_tag
def get_custom_admin_css():
    global _compiled_sass
    if not _compiled_sass:
        _compiled_sass = sass.compile(string=get_sass_source())
    return _compiled_sass
