from django.test import TestCase
from product.models import Cart,Stock
class StockTestcases(TestCase):
    def setUp(self):
        Stock.objects.create(prodid=1000,tot_qty=20,last_update=22-10-2020,next_update=22-10-2029)
    def test_Stock_info(self):
        s1 = Stock.objects.all()
        self.assertEqual(s1.get_prodid(),1005)
        # self.assertEqual(s1.get_tot_qty(),20)
        # self.assertEqual(s1.get_last_update(),22-10-2020)
        # self.assertEqual(s1.get_next_update(),22-10-2029)
