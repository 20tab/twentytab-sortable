from django.test import TestCase
from sortable.models import PositionModel


class SortableTestCase(TestCase):
    """
    add sortable to INSTALLED_APPS to run the following tests !!!
    """

    class IAMSortable(PositionModel):
        class Meta:
            ordering = ('position',)

    def test_ordering(self):
        s0 = self.IAMSortable()
        s0.position = 1
        s0.save()
        s1 = self.IAMSortable()
        s1.position = 0
        s1.save()
        all_sortable = self.IAMSortable.objects.all()
        self.assertEqual(all_sortable[0].position, 0)
        self.assertEqual(all_sortable[1].position, 1)
        return s0, s1

    def test_max_pos(self):
        s0, s1 = self.test_ordering()
        s2 = self.IAMSortable()
        s2.position = 999
        s2.save()
        self.assertEqual(s0.max_pos, 1000)
        s2.delete()
        self.assertEqual(s0.max_pos, 2)

