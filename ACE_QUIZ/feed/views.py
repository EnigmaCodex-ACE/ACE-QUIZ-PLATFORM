from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
# Create your views here.

def main_feed(request):
    html = "<html><body>This is Main Feed being added for now</body></html>"
    return HttpResponse(html)