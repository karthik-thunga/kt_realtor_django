from django.urls import path
from .views import Index, about

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', about, name='about'),
]
