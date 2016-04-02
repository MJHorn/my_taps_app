from django.shortcuts import render

def tap_list(request):
    return render(request, 'taplists/tap_list.html', {})
