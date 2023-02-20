from django.shortcuts import render
from django.http import FileResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def download(request):
    img = open('files/Abdurahmonov Jamshid.doc', 'rb')

    response = FileResponse(img)

    return response
