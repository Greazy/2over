from django.urls import path
from .import views


urlpatterns = [
    path('', views.userList, name="users"),
    path('<int:pk>/detail/', views.getUser, name="user"),
    path('create/', views.createUser, name="create"),
    path('<int:pk>/update/', views.updateUser, name="update"),
    path('<int:pk>/delete/', views.deleteUser, name="delete")
]
