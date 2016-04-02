from django.shortcuts import render
from .models import Tap

def tap_list(request):
    taps = Tap.objects.order_by('-rating')[:5]
    return render(request, 'taplists/tap_list.html', {'taps': taps})
