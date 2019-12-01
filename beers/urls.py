from django.conf.urls import url

from beers.views import beer_list_view, beer_detail_view

urlpatterns = [
    url(r"^list/$", beer_list_view, name='beer-list-view'),
    url(r"^detail/(?P<pk>\d+)$", beer_detail_view, name='beer-detail-view')
]