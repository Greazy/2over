from django.urls import path
from todo import views


urlpatterns = [
    path("", views.ListTodoAPIView.as_view(), name="todo_list"),
    path("create/", views.CreteTodoAPIView.as_view(), name="todo_create"),
    path("update/<int:pk>/", views.UpdateTodoAPIView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", views.DeleteTodoAPIView.as_view(), name="todo_delete"),
]
