from unicodedata import name
from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cvsite, name="home"),
    path('contatti', views.contatti, name="contatti"),
    path('curriculum', views.curriculum, name="curriculum"),
    path('cv-download/', views.download_file, name="cv-download"),
    path('detail/<int:cvelement_id>', views.detail, name='detail'),
]
