from django.core import exceptions
from django.test import TestCase

import catalog.models

__all__ = []


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.spot = catalog.models.Spot.objects.create(
            name="Озеро",
            text="test",
            lon=20.123,
            lat=34.128,
        )

    def test_spotlenname_fail(self):
        item_count = catalog.models.Spot.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            item = catalog.models.Spot(
                name="a" * 151,
                text="роскошно",
            )
            item.full_clean()
            item.save()
        self.assertEqual(catalog.models.Spot.objects.count(), item_count)
