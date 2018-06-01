# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from  first_app.forms import URLForm
from  first_app.models import  Topic
import string
import random
from django.core.urlresolvers import reverse
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
           short_url=id_generator();
           topic.short_url=short_url;
           topic.save();
           return render(request,"form.html",{"form":form,"short_url":"http://127.0.0.1:8000/"+short_url})
        else:
           return render(request,"form.html",{"form":form})

    return render(request,"form.html",{"form":form})
def id_generator(size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def  redirect(request):
     url=request.get_full_path()
     short_url=url[1:]
     print url
     print short_url

     topic=Topic.objects.get(short_url=short_url)
     print short_url
     return   HttpResponseRedirect(topic.url_name)
