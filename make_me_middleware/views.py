from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    context = {}
    return TemplateResponse(request, template="index.html", context=context)