from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def credits(request):
    content = 'Nicky\nYour  Name'
    return HttpResponse(content=content, content_type='text/plain')
    


def about_page(request):
    content = 'Our company is multinational\n multiculturalism'
    return HttpResponse(content=content, content_type='HTML')

def version_info(request):
    content = f'Latest version: {1}'
    return JsonResponse(content, safe=False)