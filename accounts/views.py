from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):
    return render(request, 'accounts/home.html')


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang-"en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
