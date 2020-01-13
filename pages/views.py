from django.shortcuts import render
from django.views.generic import ListView
from listings.models import Listings
from realtors.models import Realtor


class index(ListView):
    model = Listings
    template_name = 'pages/index.html'
    context_object_name = 'listings'
    ordering = '-list_date'
    paginate_by = 3


def about(request):
    context = {
        'realtors': Realtor.objects.all()
    }
    return render(request, 'pages/about.html', context)
