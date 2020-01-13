from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Listings


class ListingsView(ListView):
    model = Listings
    template_name = 'listings/listings.html'
    context_object_name = 'listings'
    paginate_by = 3


class ListingdetailView(DetailView):
    model = Listings
    template_name = 'listings/listing.html'
    context_object_name = 'listing'


def search(request):
    return render(request, 'listings/search.html')
