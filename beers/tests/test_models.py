from django.test import TestCase

# Create your tests here.
from beers.models import Company, Beer


class BasicTestClass(TestCase):
    @classmethod
    def setUpTestData(self):
        company = Company.objects.create(name='comp', tax_number=98)
        Beer.objects.create(name='be', company=company)
        Beer.objects.create(name='be1', company=company)
        Beer.objects.create(name='be2', company=company)

    def setUp(self):
        print("setUp")

    # def test_is_alcoholiic(self):
    #     beer = Beer.objects.get(pk=1)
    #     self.assertEquals(beer.is_alcoholic, True)
    #
    # def test_has_more_alcohol_than(self):
    #     beer = Beer.objects.get(pk=1)
    #     self.assertTrue(beer.has_more__alcohol_than(4), True)
