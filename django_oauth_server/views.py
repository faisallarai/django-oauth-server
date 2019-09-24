from django.shortcuts import render, redirect

def home(request):
    return redirect('oauth2_provider:list')