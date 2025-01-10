from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loading/<str:linkKey>/', views.loading_screen, name='loading_screen'),
    path('success/<str:linkKey>/', views.success_page, name='success_page'),
    path('valida_link/', views.valida_link, name='valida_link'),
    path('<str:link>/', views.redirecionar, name='redirecionar'),
]
