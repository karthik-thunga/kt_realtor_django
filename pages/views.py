from django.shortcuts import render
from django.views.generic import ListView
from listings.models import Listings
from realtors.models import Realtor
from listings.choices import bedroom_choices, state_choices, price_choices


class Index(ListView):
    model = Listings
    template_name = 'pages/index.html'
    context_object_name = 'listings'
    ordering = '-list_date'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['bedroom_choices'] = bedroom_choices
        context['state_choices'] = state_choices
        context['price_choices'] = price_choices
        return context


def about(request):
    context = {
        'realtors': Realtor.objects.all(),
        'mvp_realtors': Realtor.objects.filter(is_mvp=True).first()
    }
    return render(request, 'pages/about.html', context)
