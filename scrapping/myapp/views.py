from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests 
from .models import Link 
from django.http import HttpResponseRedirect
# Create your views here.



def scrape(request):
    data = None
    if request.method == "POST":
        site = request.POST.get('site','')
        if 'https://' not in site:
            site = 'https://' + site
            page =requests.get(site)
            
            soup = bs(page.text,'html.parser')

            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_text = link.string
                Link.objects.create(address=link_address, name=link_text)
            return HttpResponseRedirect('/')
    else:
        
        data = Link.objects.all().order_by('name')

    return render(request,'myapp/result.html',{'data':data})

def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')