from django.conf.urls import url
from django.urls import include

from beers.views import BeerListView, BeerDetailView, company_edit

urlpatterns = [
    url(r"^list/$", BeerListView.as_view(), name='beer-list-view'),
    url(r"^detail/(?P<pk>\d+)$", BeerDetailView.as_view(), name='beer-detail-view'),
    url(r"^company/edit/(?P<pk>\d+)$", company_edit, name='company-edit-view')
]
