# predictor/urls.py
# from django.urls import path
# from .views import  result, home 

# urlpatterns = [
#     path('', home, name='home'),  
#     path('result/', result, name='result'),
# ]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('result/', views.result, name='result'),  # Result page
]
