from django.urls import path
from . import views

app_name = 'coffee-api'

urlpatterns = [
    # to request to this view go to "http://127.0.0.1:8000/api/coffee/machines"
    path('machines', views.CoffeeMachines.as_view(), name='coffee_machines'),
    # to request to this view go to "http://127.0.0.1:8000/api/coffee/pods"
    path('pods', views.CoffeePods.as_view(), name='coffee_pods'),
]