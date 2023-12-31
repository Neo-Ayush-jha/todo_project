from django.urls import path
from .views import TodoItemListView, TodoItemDetailView

urlpatterns = [
    path('todos/', TodoItemListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoItemDetailView.as_view(), name='todo-detail'),
]
