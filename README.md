twentytab-sortable
==================

A django model and admin to create sortable items in django admin with jqueryui sortable method

## Installation

Use the following command: <b><i>pip install twentytab-sortable</i></b>

## Configuration

- Settings.py

Open settings.py and add sortable to your INSTALLED_APPS:

```py
INSTALLED_APPS = [
    ...
    'sortable',
    ...
]
```

- Static files

Run collectstatic command or map static directory.

## Usage
- models.py

```py
from sortable.models import PositionModel


class MyPositionModel(PositionModel):
    pass

```

- admin.py

```py
from django.contrib import admin
from myapp.models import MyPositionModel
from sortable.admin import PositionAdmin, SortableTabularInline, SortableStackedInline

class MyTabularInline(SortableTabularInline):
    # add 'position' in your fields
    model = APositionModel

class MyStackedInline(SortableStackedInline):
    # add 'position' in your fields
    model = APositionModel

class MyPositionAdmin(PositionAdmin):
    inlines = [MyTabularInline, MyStackedInline]
    # add 'position' in your list_editable fields

admin.site.register(MyPositionModel, MyPositionAdmin)


```
