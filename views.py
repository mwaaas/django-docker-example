from django.shortcuts import render

def home(request):
  c = {'hello': 'world'}
  response = render(request, 'home.html', c )
  return response

def another(request):
  c = {}
  response = render(request, 'another.html', c )
  return response

def onemore(request):
  c = {}
  response = render(request, 'onemore.html', c )
  return response
