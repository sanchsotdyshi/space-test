from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('', views.test, name='test'),
    path('check/', views.check, name='check'),
    path('form/<int:score>', views.form, name='form'),
    path('form/<int:score>/<int:war>/', views.form, name='war_form'),
    path('registration/<int:score>', views.registration, name='registration'),
    #path('form/<int:war>/', views.form, name='war_form'),
    #path('registration/', views.registration, name='registration'),

]