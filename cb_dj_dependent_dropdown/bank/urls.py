from django.urls import path

from . import views


app_name='bank'


urlpatterns = [
    path('index/',views.index,name='index'),
    # path('add/', views.person_create_view, name='person_add'),
    # path('details/<int:movie_id>/', views.detail, name='detail'),
    path('',views.index,name='index'),
    path('home',views.index2,name='index2'),
    path('login/',views.login,name='login'),
    path('reg/',views.register,name='register'),
    path('persons/add/',views.show,name='show'),


    # path('red/',views.page,name='page'),

]