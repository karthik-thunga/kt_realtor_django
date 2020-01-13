from django.urls import path
from .views import ListingsView, ListingdetailView, search

urlpatterns = [
    path('', ListingsView.as_view(), name='listings'),
    path('<int:pk>', ListingdetailView.as_view(), name='listing'),
    path('search', search, name='search'),
]
