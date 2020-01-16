from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Listings
from .choices import state_choices, price_choices, bedroom_choices


class ListingsView(ListView):
    model = Listings
    template_name = 'listings/listings.html'
    context_object_name = 'listings'
    paginate_by = 4


class ListingdetailView(DetailView):
    model = Listings
    template_name = 'listings/listing.html'
    context_object_name = 'listing'


def search(request):
    listings = Listings.objects.order_by("-list_date")
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    if 'state' in request.GET:
        state_code = request.GET['state']
        state = state_choices[state_code]
        if state:
            listings = listings.filter(state=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms=bedrooms)

    if 'price' in request.GET:
        max_price = request.GET['price']
        if max_price:
            listings = listings.filter(price__lte=max_price)
    context = {
        "listings": listings,
        "state_choices": state_choices,
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices,
        "values": request.GET
    }
    return render(request, 'listings/search.html', context)
