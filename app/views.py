from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForms()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForms(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is done Successfully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage is done')

    return render(request,'insert_webpage.html',d)

def insert_AccessRecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}

    if request.method=='POST':
        ARDO=AccessRecordForm(request.POST)
        if ARDO.is_valid():
            ARDO.save()
            return HttpResponse('insert_AccessRecord is ok')

    return render(request,'insert_AccessRecord.html',d)
