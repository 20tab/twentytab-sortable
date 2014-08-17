from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import conf


class PositionModel(models.Model):
    """
    It's an abstract model to create sortable items in list_display or in inline admin
    """
    position = models.PositiveIntegerField(_(u'Position'), default=0)

    def __unicode__(self):
        return u"%s %s" % (self.__class__.__name__, self.position)

    @property
    def max_pos(self):
        max_number_instance = self.__class__.objects.aggregate(models.Max('position'))['position__max']
        if max_number_instance:
            return max_number_instance + 1
        else:
            return 1

    def save(self, *args, **kwargs):
        if self.position == 0:
            self.position = self.max_pos
        super(PositionModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
