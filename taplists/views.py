from django.db.models import Count
from django.http import QueryDict
from django.shortcuts import render
from .models import Tap
from .models import Bar
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import TapForm
from .forms import StyleForm
from .filterset import TapFilter
from .filterset import TapFilterMin
from .filterset import MTapFilter
from .filterset import IOSTapFilter
from .filterset import IOSTapFilterMin
from .filterset import MTapFilterMin
from django.views.generic.list import ListView
from django.template import RequestContext
from django.db.models import Prefetch

def home(request):
    if request.flavour == "mobile":
        template='taplists/home_m.html' 
    elif request.flavour == 'ios':
        template='taplists/home_m.html' 
    else:
        template='taplists/home.html'

    return render(request, template)

def home_draft(request):
    if request.flavour == "mobile":
        template='taplists/home_draft_m.html' 
    else:
        template='taplists/home_draft.html'

    return render(request, template)

def tap_list(request):
    if request.flavour == "ios":
        prefetch =  Prefetch(
        'bar', 
        queryset=Bar.objects.filter(state="VIC"),
        to_attr='selected_states'
        )    
        f = IOSTapFilter(request.GET, queryset=Tap.objects.filter(bar__state="VIC").distinct().prefetch_related(prefetch).order_by('-rating'))
        template='taplists/ios_tap_list.html'
        page_template='taplists/ios_tap_list_page.html'

    elif request.flavour == "mobile":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="VIC"),
       to_attr='selected_states'
       )   
       f = MTapFilter(request.GET, queryset=Tap.objects.filter(bar__state="VIC").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/m_tap_list.html'
       page_template='taplists/m_tap_list_page.html'
    else:
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="VIC"),
       to_attr='selected_states'
       )
       f = TapFilter(request.GET, queryset=Tap.objects.filter(bar__state="VIC").distinct().prefetch_related(prefetch))
       template='taplists/tap_list.html'
       page_template='taplists/tap_list_page.html'

    taps = Tap.objects.order_by('-rating')
    b = request.GET.getlist('bar__region')

    context = {
            'taps': taps,'filter': f, 'page_template' : page_template, 'placename' : 'Melbourne/Victoria', 'state' : 'VIC', 'regions' : b
    } 
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))
    
def tap_NSW(request):

    if request.flavour == "mobile":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="NSW"),
       to_attr='selected_states'
       )   
       f = MTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="NSW").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/m_tap_list_NSW.html'
       page_template='taplists/m_tap_list_page.html'
    elif request.flavour == "ios":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="NSW"),
       to_attr='selected_states'
       )   
       f = IOSTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="NSW").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/ios_tap_list_OTH.html'
       page_template='taplists/ios_tap_list_page.html'

    else:
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="NSW"),
       to_attr='selected_states'
       )   
       f = TapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="NSW").distinct().prefetch_related(prefetch))
       template='taplists/tap_list_NSW.html'
       page_template='taplists/tap_list_page.html'

    taps = Tap.objects.order_by('-rating')

    context = {
            'taps': taps,'filter': f, 'page_template' : page_template, 'placename' : 'Sydney/New South Wales', 'state' : 'NSW'
    } 
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))
   
def tap_QLD(request):

    if request.flavour == "mobile":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="QLD"),
       to_attr='selected_states'
       )   
       f = MTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="QLD").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/m_tap_list_NSW.html'
       page_template='taplists/m_tap_list_page.html'
    elif request.flavour == "ios":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="QLD"),
       to_attr='selected_states'
       )   
       f = IOSTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="QLD").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/ios_tap_list_OTH.html'
       page_template='taplists/ios_tap_list_page.html'
    else:
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="QLD"),
       to_attr='selected_states'
       )   
       f = TapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="QLD").distinct().prefetch_related(prefetch))
       template='taplists/tap_list_NSW.html'
       page_template='taplists/tap_list_page.html'

    taps = Tap.objects.order_by('-rating')

    context = {
            'taps': taps,'filter': f, 'page_template' : page_template, 'placename' : 'Brisbane/Queensland', 'state' : 'QLD'
    } 
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))
 
def tap_ACT(request):

    if request.flavour == "mobile":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="ACT"),
       to_attr='selected_states'
       )   
       f = MTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="ACT").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/m_tap_list_NSW.html'
       page_template='taplists/m_tap_list_page.html'
    elif request.flavour == "ios":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="ACT"),
       to_attr='selected_states'
       )   
       f = IOSTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="ACT").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/ios_tap_list_OTH.html'
       page_template='taplists/ios_tap_list_page.html'
    else:
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="ACT"),
       to_attr='selected_states'
       )   
       f = TapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="ACT").distinct().prefetch_related(prefetch))
       template='taplists/tap_list_NSW.html'
       page_template='taplists/tap_list_page.html'

    taps = Tap.objects.order_by('-rating')

    context = {
            'taps': taps,'filter': f, 'page_template' : page_template, 'placename' : 'Canberra/ACT', 'state' : 'ACT'
    } 
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))

def tap_WA(request):

    if request.flavour == "mobile":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="WA"),
       to_attr='selected_states'
       )   
       f = MTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="WA").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/m_tap_list_NSW.html'
       page_template='taplists/m_tap_list_page.html'
    elif request.flavour == "ios":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="WA"),
       to_attr='selected_states'
       )   
       f = IOSTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="WA").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/ios_tap_list_OTH.html'
       page_template='taplists/ios_tap_list_page.html'
    else:
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="WA"),
       to_attr='selected_states'
       )   
       f = TapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="WA").distinct().prefetch_related(prefetch))
       template='taplists/tap_list_NSW.html'
       page_template='taplists/tap_list_page.html'

    taps = Tap.objects.order_by('-rating')

    context = {
            'taps': taps,'filter': f, 'page_template' : page_template, 'placename' : 'Perth/WA', 'state' : 'WA'
    } 
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))

def tap_TAS(request):

    if request.flavour == "mobile":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="TAS"),
       to_attr='selected_states'
       )   
       f = MTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="TAS").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/m_tap_list_NSW.html'
       page_template='taplists/m_tap_list_page.html'
    elif request.flavour == "ios":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="TAS"),
       to_attr='selected_states'
       )   
       f = IOSTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="TAS").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/ios_tap_list_OTH.html'
       page_template='taplists/ios_tap_list_page.html'
    else:
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="TAS"),
       to_attr='selected_states'
       )   
       f = TapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="TAS").distinct().prefetch_related(prefetch))
       template='taplists/tap_list_NSW.html'
       page_template='taplists/tap_list_page.html'

    taps = Tap.objects.order_by('-rating')

    context = {
            'taps': taps,'filter': f, 'page_template' : page_template, 'placename' : 'Hobart/TAS', 'state' : 'TAS'
    } 
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))

def tap_SA(request):

    if request.flavour == "mobile":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="SA"),
       to_attr='selected_states'
       )   
       f = MTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="SA").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/m_tap_list_NSW.html'
       page_template='taplists/m_tap_list_page.html'
    elif request.flavour == "ios":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="SA"),
       to_attr='selected_states'
       )   
       f = IOSTapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="SA").distinct().prefetch_related(prefetch).order_by('-rating'))
       template='taplists/ios_tap_list_OTH.html'
       page_template='taplists/ios_tap_list_page.html'
    else:
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.filter(state="SA"),
       to_attr='selected_states'
       )   
       f = TapFilterMin(request.GET, queryset=Tap.objects.filter(bar__state="SA").distinct().prefetch_related(prefetch))
       template='taplists/tap_list_NSW.html'
       page_template='taplists/tap_list_page.html'

    taps = Tap.objects.order_by('-rating')

    context = {
            'taps': taps,'filter': f, 'page_template' : page_template, 'placename' : 'Adelaide/SA', 'state' : 'SA'
    } 
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))

def tap_ALL(request):

    if request.flavour == "mobile":
       f = MTapFilterMin(request.GET, queryset=Tap.objects.exclude(bar__isnull=True).order_by('-rating'))
       template='taplists/m_tap_list_ALL.html'
       page_template='taplists/m_tap_list_ALL_page.html'
    elif request.flavour == "ios":
       prefetch =  Prefetch(
       'bar', 
       queryset=Bar.objects.all(),
       to_attr='selected_states'
       )   
       f = IOSTapFilterMin(request.GET, queryset=Tap.objects.exclude(bar__isnull=True))
       template='taplists/ios_tap_list_OTH.html'
       page_template='taplists/ios_tap_list_page.html'
    else:
       f = TapFilterMin(request.GET, queryset=Tap.objects.exclude(bar__isnull=True))
       template='taplists/tap_list_ALL.html'
       page_template='taplists/tap_list_allpage.html'

    taps = Tap.objects.order_by('-rating')
    form = TapForm()

    context = {
            'taps': taps,'form': form,'filter': f, 'page_template' : page_template, 'placename' : 'Australia', 'state' : 'ALL'
    } 
    if request.is_ajax():
        template = page_template
    return render(request, template, context, context_instance=RequestContext(request))

def stats(request):
    taps = Tap.objects.annotate(posts=Count('bar')).order_by('-posts')[:20]
    template = 'taplists/tap_list.html'
    page_template = 'taplists/stats_page.html'
    return render(request, template, {'taps' : taps, 'page_template' : page_template}, context_instance=RequestContext(request))



def cookie(request):
    return render(request, 'taplists/cookie.html')

