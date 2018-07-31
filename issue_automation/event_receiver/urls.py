from django.urls import path
from . views import *

urlpatterns = [
    path('receive/',receive_event,name="receive event payload")
]