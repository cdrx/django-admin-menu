# Django Admin Menu Theme

An alternative theme for the Django admin that has a horizontal navigation bar with drop down menus for your models.

![screenshot](screenshots/drop-down.png)

## Installation

Install the package:

```
pip install django-admin-menu
```

Then add `admin_menu` to your `INSTALLED_APPS` setting, **before `django.contrib.admin`** (or it wont work). For example:

```
INSTALLED_APPS = [
    'admin_menu',
    'django.contrib.admin',
    ...
]
```

## Settings

There are a couple of options you can adjust in your `settings.py` to influence the theme.

To adjust the logo, change:
```
ADMIN_LOGO = 'logo.png'
```

The logo is used in the top left of each page and on the login page.

You can adjust the order of the menu items with the `MENU_WEIGHT` setting:

```
MENU_WEIGHT = {
    'World': 20,
    'Auth': 4,
    'Sample': 5
}
```

Items with a higher weight will be pushed to the end of the menu. You don't have to fill in all the menu items, just the ones you would like to adjust the position of.

### ModelAdmin Settings

There are a few settings on your `ModelAdmin` class to adjust the menu:

```
class MyAdmin(admin.ModelAdmin):
    menu_title = "Users"
    menu_group = "Staff"
```

will change the title for this model to `Users` and place it on a drop down titled `Staff`.

You can use the same `menu_group` on multiple `ModelAdmin` classes and they will be grouped on the same menu.

## Screenshots

![screenshot](screenshots/login.png)
![screenshot](screenshots/form.png)
![screenshot](screenshots/drop-down.png)

## Theming



![screenshot](screenshots/ui-dark.png)
![screenshot](screenshots/ui-green.png)
![screenshot](screenshots/ui-red.png)
