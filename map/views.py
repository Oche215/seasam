from django.shortcuts import render

# Create your views here.
def maps(request):
    return render(request, 'map/maps.html', {})
