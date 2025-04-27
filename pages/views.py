import json

from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q, Max

from django_project.settings import EMAIL_HOST_USER, DEFAULT_FROM_EMAIL
from .models import NigeriaMineralDeposit, GeoPoliticalRegion, Minerals
from connect.models import Connect

from .forms import ContactUsForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {} )

def about(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)

        address = request.POST.get('email')
        subject = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        attachment = request.FILES.get('file')

        if address and subject and message:
            try:
                send_mail(f'Inquiry from {subject}',f'From: {address}\nName: {subject} \nPhone: {phone} \nMessage: {message}', DEFAULT_FROM_EMAIL, ['exploration.seasam@outlook.com'], html_message=attachment)
                messages.success(request, 'Email sent successfully')
            except Exception as e:
                messages.success(request, f'Error sending email {e}')
        else:
            messages.success(request, 'All fields are required to send us a note except for File')


        if form.is_valid():
            form.save()

            messages.success(request, 'Your messages uploaded successfully!')
            return render(request, 'home.html', {'form': form})
        else:
            return render(request, 'contact.html', {'form': form})

    else:
        return render(request, 'about.html', {'form': form})


def log(request):
    px  = Connect.objects.all().count()

    price = Connect.objects.filter(id=px)
    return render(request, 'logistics.html', {'price': price})

def contract(request):
    return render(request, 'econtract.html', {})

def contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your messages uploaded successfully!')
            return render(request, 'home.html', {'form': form})
        else:
            return render(request, 'contact.html', {'form': form})

    else:
        return render(request, 'contact.html', {'form': form})


def mineral(request):
    if request.user.is_authenticated:
        minerals = NigeriaMineralDeposit.objects.all()
        return render(request, 'minerals/mineral.html', {'minerals': minerals})
    else:
        messages.success(request, 'Your are not allowed to view this page contact the Site Admin!')
        form = ContactUsForm()
        if request.method == 'POST':
            form = ContactUsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your messages uploaded successfully!')
                return render(request, 'home.html', {'form': form})
            else:
                return render(request, 'contact.html', {'form': form})

        else:
            return render(request, 'contact.html', {'form': form})


def mineral_detail(request, pk):
    if request.user.is_authenticated:

        mineral = NigeriaMineralDeposit.objects.get(id=pk)
        return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})
    else:
        messages.success(request, 'Your are not allowed to view this page contact the Site Admin!')
        return render(request, 'contact.html', {})

def minerals(request):
    minerals = Minerals.objects.all()
    return render(request, 'minerals/minerals.html', {'minerals': minerals})

def mineral_description(request, pk):
    mineral = Minerals.objects.get(id=pk)
    states = NigeriaMineralDeposit.objects.filter(minerals__icontains=mineral)

    return render(request, 'minerals/mineral_description.html', {'mineral': mineral, 'states': states})


def search(request):
    if request.method == 'POST':
        s = request.POST['searched']
        if s == '':
            messages.error(request, f'Your search entry cannot be empty {s}!')
            return render(request, 'minerals/search.html', {})
        else:
            searched = NigeriaMineralDeposit.objects.filter(Q(minerals__icontains=s) | Q(note__icontains=s) | Q(state__icontains=s)).order_by('region')

            if not searched:
                messages.success(request, f'Sorry, "{s}" did not return any result!')
                return render(request, 'minerals/search.html', {'s':s})
        return render(request, 'minerals/search.html', {'searched': searched, 's': s})

    else:

        products = NigeriaMineralDeposit.objects.all()
        return render(request, 'minerals/search.html', {'product': products})


def ne(request):
    foo =  'North-East'
    region = GeoPoliticalRegion.objects.get(region=foo)
    cat = NigeriaMineralDeposit.objects.filter(region=region)

    return render(request, 'minerals/region.html', {'cat': cat, 'foo': foo})

def se(request):
    foo =  'South-East'
    region = GeoPoliticalRegion.objects.get(region=foo)
    cat = NigeriaMineralDeposit.objects.filter(region=region)

    return render(request, 'minerals/region.html', {'cat': cat, 'foo': foo})

def sw(request):
    foo =  'South-West'
    region = GeoPoliticalRegion.objects.get(region=foo)
    cat = NigeriaMineralDeposit.objects.filter(region=region)

    return render(request, 'minerals/region.html', {'cat': cat, 'foo': foo})

def mb(request):
    foo =  'Middle-Belt'
    region = GeoPoliticalRegion.objects.get(region=foo)
    cat = NigeriaMineralDeposit.objects.filter(region=region)

    return render(request, 'minerals/region.html', {'cat': cat, 'foo': foo})

def ss(request):
    foo =  'South-South'
    region = GeoPoliticalRegion.objects.get(region=foo)
    cat = NigeriaMineralDeposit.objects.filter(region=region)

    return render(request, 'minerals/region.html', {'cat': cat, 'foo': foo})

def nw(request):
    foo =  'North-West'
    region = GeoPoliticalRegion.objects.get(region=foo)
    cat = NigeriaMineralDeposit.objects.filter(region=region)

    return render(request, 'minerals/region.html', {'cat': cat, 'foo': foo})


def mineral_description_states(request, pk):
    mineral = Minerals.objects.get(id=pk)
    states = NigeriaMineralDeposit.objects.filter(minerals__icontains=mineral)

    return render(request, 'minerals/mineral_description_states.html', {'mineral': mineral, 'states': states})