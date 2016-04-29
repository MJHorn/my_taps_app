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
from django.template import RequestContext

def tap_list(request):
    taps = Tap.objects.order_by('-rating')
    form = TapForm()
    template='taplists/tap_list.html'
    page_template='taplists/tap_list_page.html'
    f = TapFilter(request.GET, queryset=Tap.objects.all())
    context = {
    'taps': taps,'form': form,'filter': f, 'page_template' : page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))

def cookie(request):
    return render(request, 'taplists/cookie.html')

def tap_style(request):
    taps = Tap.objects.order_by('-rating')
    form = StyleForm()
    f = StyleFilter(request.GET, queryset=Tap.objects.all())
    return render(request, 'taplists/tap_style.html', {'taps': taps,'form': form,'filter': f})
