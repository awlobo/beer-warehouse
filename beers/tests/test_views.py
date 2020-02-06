from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy

from beers.models import Company


class CompanyListViewTests(TestCase):
    def setUp(self):
        mommy.make(Company, _quantity=12)
        self.user = mommy.make(User)

    def test_view_url_exist(self):
        url = '/beers/company/list/'
        self.client.force_login(self.user)
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_view_returns_all_views(self):
        url = '/beers/company/list/'
        self.client.force_login(self.user)
        resp = self.client.get(url)
        self.assertEquals(resp.context['object_list'].count(), Company.objects.all().count())

    def check_plantilla(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('company-list-view'))
        self.assertTemplateUsed(resp, 'beers/company_list.html')

    # def test_login_check_plantilla(self):
    #     #self.client.force.login(User.objects.first())
    #     resp = self.client.get(reverse('company-list-view'))
    #     self.assertEquals(resp.status_code, 302)


