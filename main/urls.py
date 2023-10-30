from django.urls import path
from main.views import HomeView, TodoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('todo/', TodoView.as_view(), name='todo'),
]