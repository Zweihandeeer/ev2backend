from django.contrib import admin
from django.urls import path
from velasquezluis import views

# Rutas en las por las que se irán redireccionando los métodos y las views.
urlpatterns = [
    path('', views.home, name='Home'),
    path('nuevo_chat/', views.nuevo_chat, name='New'),
    path('login/', views.login, name='Login'),
    path('logout/', views.logout, name='Logout'),
    path('admin/', admin.site.urls),
]
