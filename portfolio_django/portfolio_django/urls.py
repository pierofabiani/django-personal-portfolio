from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cvsite, name="home"),
    path('contatti', views.contatti, name="contatti")
]
