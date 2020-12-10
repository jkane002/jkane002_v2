from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    """base page"""
    return HttpResponse('<h1>Testing</h1>')
