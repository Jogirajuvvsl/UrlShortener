# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from  first_app.forms import URLForm
from  first_app.models import  Topic
import hashlib
import base64
# Create your views here.
def index(request):
    return render(request,"index.html",{"value":"RAJU"})

def form_request(request):
    form=URLForm();
    if request.method=="POST":
        form=URLForm(request.POST)

        if(form.is_valid):
           topic=form.save(commit=False)
           hash=hashlib.md5()
           print topic.url_name

           topic.short_url=hashlib.md5(topic.url_name.encode('utf-8')).hexdigest()
           short_url=base64.b64encode(topic.short_url)
           topic.save();
           return render(request,"form.html",{"form":form,"short_url":short_url})
        else:
           return render(request,"form.html",{"form":form})

    return render(request,"form.html",{"form":form})
