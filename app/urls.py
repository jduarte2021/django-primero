from django.urls import path     
from . import views
urlpatterns = [


    path('', views.root),
    path('blogs/', views.blogs),
    path('blogs/new/', views.new),
    path('blogs/create/', views.create),
    path('blogs/<int:number>', views.number),
    path('blogs/<int:number>/edit/', views.edit),
    path('blogs/<int:number>/delete/', views.destroy),
    path('blogs/json/', views.index),

]