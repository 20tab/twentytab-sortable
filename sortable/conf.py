from appconf import AppConf
from django.conf import settings


class SortableConf(AppConf):
    JQUERY_LIB = u"{}{}".format(
        getattr(settings, u'STATIC_URL', u'/static/'),
        u"sortable/js/jquery-2.1.0.min.js"
    )
    JQUERYUI_LIB = u"{}{}".format(
        getattr(settings, u'STATIC_URL', u'/static/'),
        u"sortable/jquery-ui-1.10.4.custom/js/jquery-ui-1.10.4.custom.min.js"
    )
    JQUERYUI_CSSLIB = u"{}{}".format(
        getattr(settings, u'STATIC_URL', u'/static/'),
        u"sortable/jquery-ui-1.10.4.custom/css/smoothness/jquery-ui-1.10.4.custom.min.css"
    )

    def configure_jquery_lib(self, value):
        if not getattr(settings, 'JQUERY_LIB', None):
            self._meta.holder.JQUERY_LIB = value
            return value
        return getattr(settings, 'JQUERY_LIB')

    def configure_jqueryui_lib(self, value):
        if not getattr(settings, 'JQUERYUI_LIB', None):
            self._meta.holder.JQUERYUI_LIB = value
            return value
        return getattr(settings, 'JQUERYUI_LIB')

    def configure_jqueryui_csslib(self, value):
        if not getattr(settings, 'JQUERYUI_CSSLIB', None):
            self._meta.holder.JQUERYUI_CSSLIB = value
            return value
        return getattr(settings, 'JQUERYUI_CSSLIB')