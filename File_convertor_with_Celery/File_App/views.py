from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# from .task import *

from django.core.files.storage import FileSystemStorage
import os
from docx2pdf import convert

# Create your views here.

def index(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name , myfile)
        print(filename, "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        uploaded_file_url = fs.url(filename)
        convert(myfile.name) 
    return render(request, 'home.html')
