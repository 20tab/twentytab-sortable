from django.contrib import admin
from django.conf import settings
from django.contrib.admin import TabularInline, StackedInline


class PositionAdmin(admin.ModelAdmin):
    """
    Abstract admin option class for PositionModel
    """
    list_display = ('position', 'pk')
    list_editable = ('position',)
    list_display_links = ('pk',)
    ordering = ('position',)
    exclude = ('position',)

    class Media:
        js = (settings.JQUERY_LIB,
              settings.JQUERYUI_LIB,
              u'{}sortable/js/admin-list-reorder.js'.format(settings.STATIC_URL),)

    class Meta:
        abstract = True


class SortableStackedInline(StackedInline):
    """Adds necessary media files to regular Django StackedInline"""
    extra = 0

    class Media:
        css = {u"all": (u"{}sortable/css/inline-reorder.css".format(settings.STATIC_URL),)}
        js = (settings.JQUERY_LIB,
              settings.JQUERYUI_LIB,
              u'{}sortable/js/inline-reorder.js'.format(settings.STATIC_URL),)


class SortableTabularInline(TabularInline):
    """Adds necessary media files to regular Django TabularInline"""
    extra = 0

    class Media:
        css = {u"all": (u"{}sortable/css/inline-reorder.css".format(settings.STATIC_URL),)}
        js = (settings.JQUERY_LIB,
              settings.JQUERYUI_LIB,
              u'{}sortable/js/inline-reorder.js'.format(settings.STATIC_URL),)