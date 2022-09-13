from django.urls import path
from . import views

urlpatterns = [
    path('', views.cvsite, name='home'),
    path('contatti', views.contatti, name='contatti')
]
