from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect("blogs/")
def blogs(request):
    return HttpResponse("<h1>Placeholder para luego mostrar una lista de todos los blogs</h1>")
def new(request):
    return HttpResponse("<h1>Placeholder para mostrar un nuevo formulario para crear un nuevo blog</h1>")
def create(request):
    return HttpResponse("<h1>CREATE</h1>")
def number(request,number):
    return HttpResponse(f"<h1>Placeholder para mostrar el blog numero: {number}</h1>")
def edit(request,number):
    return HttpResponse(f"<h1>Placeholder para editar el blog {number}</h1>")
def destroy(request,number):
    return redirect("/blogs/")
def index(request):
    return JsonResponse({'Nombre': "Jimmy"})

# Create your views here.
