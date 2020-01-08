from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import include

from beers.views import BeerListView, BeerDetailView, CompanyEditView, CompanyDetailView, CompanyListView, \
    CompanyCreateView, CompanyAndBeersCreateView

urlpatterns = [
    url(r"^list/$", login_required(BeerListView.as_view()), name='beer-list-view'),
    url(r"^detail/(?P<pk>\d+)$", BeerDetailView.as_view(), name='beer-detail-view'),

    url(r"^company/edit/(?P<pk>\d+)$", CompanyEditView.as_view(), name='company-edit-view'),
    url(r"^company/create-with-beers/$", CompanyAndBeersCreateView.as_view(), name='company-beers-create-view'),
    url(r"^company/create/$", CompanyCreateView.as_view(), name='company-create-view'),
    url(r"^company/detail/(?P<pk>\d+)$", CompanyDetailView.as_view(), name='company-detail-view'),
    url(r"^company/list/$", CompanyListView.as_view(), name='company-list-view')
]
