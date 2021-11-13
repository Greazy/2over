from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from todo.serializers import TodoSerializer
from.models import Todo


class ListTodoAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreteTodoAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer