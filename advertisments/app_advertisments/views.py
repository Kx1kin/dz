from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisments/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisments/top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse("main_page")
            return redirect(url)

    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisments/advertisement-post.html', context)