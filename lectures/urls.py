from django.urls import path
from . import views

app_name = 'lectures'
urlpatterns = [
	path('', views.main, name='main'),
    path('<int:num>', views.lecture, name='lecture'),
]