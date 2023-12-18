from django.shortcuts import render
from .models import Services, Haircuts, Promotions, Barbers


def index(request):
    template = 'index.html'
    services_list = Services.objects.all()
    haircut_list = Haircuts.objects.all()
    promotions_list = Promotions.objects.all()
    barbers_list = Barbers.objects.all()
    context = {
        'services': services_list,
        'haircuts': haircut_list,
        'promotions': promotions_list,
        'barbers': barbers_list,
    }
    return render(request, template, context)
