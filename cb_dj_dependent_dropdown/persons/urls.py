from django.urls import path

from . import views

# app_name='persons'

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('details/<int:movie_id>/', views.detail, name='detail'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]