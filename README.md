twentytab-sortable
==================

A django model and admin to create sortable items in django admin with jqueryui sortable method

## Installation

Use the following command: <b><i>pip install twentytab-sortable</i></b>

## Configuration

- Static files

Run collectstatic command or map static directory. If you use uWSGI you can map static files:

```ini
static-map = /static/sortable/=%(path_to_site_packages)/sortable/static/sortable
```

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
from sortable.admin import PositionAdmin

class MyPositionAdmin(PositionAdmin)
    pass

admin.site.register(MyPositionModel, MyPositionAdmin


```