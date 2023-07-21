from django.shortcuts import render
from django.urls import reverse
from .hash import Hasher
from django.http import JsonResponse
import json
from .models import ShortUrl
from django.shortcuts import redirect



def index(request):
    if request.method == 'GET':
        return render(request, 'index.html' )
    if request.method == 'POST':
        data = json.loads(request.body)
        long_url =  data.get('long_url', '')  # Provide a default value ('') if 'long_url' is not present
        if long_url == '':
            return JsonResponse({'error': 'Please enter a URL to shorten'}, status=400)
        
        short_url = 'http://localhost:8000/' + Hasher(long_url)
        if ShortUrl.objects.filter(short_url=short_url).exists():
            return JsonResponse({'short_url': short_url,'display': 'flex'})
        short_url_obj = ShortUrl.objects.create(short_url=short_url, long_url=long_url)
        short_url_obj.save()
        return JsonResponse({'short_url': short_url,'display': 'flex'})
    else:
        return render(request, 'index.html')


def redirect_url(request, short_url):
    short_url = 'http://localhost:8000/' + short_url
    try:
        short_url_obj = ShortUrl.objects.get(short_url=short_url)
        long_url = short_url_obj.long_url
        return redirect('http://'+long_url)
    except ShortUrl.DoesNotExist:
        return JsonResponse({'error': 'Short URL does not exist'}, status=404)





