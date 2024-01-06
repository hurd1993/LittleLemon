from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(menu_ID = 99, title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")