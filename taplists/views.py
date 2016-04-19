from django.shortcuts import render
from .models import Tap
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import TapForm
from .forms import StyleForm
from .filterset import TapFilter
from .filterset import StyleFilter
from django.views.generic.list import ListView

def tap_list(request):
    taps = Tap.objects.order_by('-rating')
    form = TapForm()
    f = TapFilter(request.GET, queryset=Tap.objects.all())
    return render(request, 'taplists/tap_list.html', {'taps': taps,'form': form,'filter': f})

def about(request):
    return render(request, 'taplists/about.html')

def tap_style(request):
    taps = Tap.objects.order_by('-rating')
    form = StyleForm()
    f = StyleFilter(request.GET, queryset=Tap.objects.all())
    return render(request, 'taplists/tap_style.html', {'taps': taps,'form': form,'filter': f})
