from django.urls import path
from .apis import *

urlpatterns = [
    path('machine/', coffee_machines.as_view(),name = 'coffee_machines'),
    path('pods/', coffee_pods.as_view(), name='coffee_pods'),
]