from os import makedirs
from django.shortcuts import render
from qrcode import *
from django.http import HttpResponse
# Create your views here.

data = None
def home(request):
    global data
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img.save("watermark/media/qrcode/test.png")
    else:
        pass
    return render(request, "home.html", {'data': data})
