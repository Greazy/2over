from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_all_articles(_request):
    articles = Blog.objects.all()
    serializer = BlogSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_article(_request, pk):
    try:
        article = Blog.objects.get(id=pk)
        serializer = BlogSerializer(article, many=False)
        return Response(serializer.data)
    except Blog.DoesNotExist:
        return Response("Article not found", status=404)

@api_view(['POST'])
def create_article(request):
    try:
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response("Oooops", status=400)
    except Exception as e:
        return Response(data=e, status=400)


@api_view(['PUT'])
def update_article(request, pk):
    pass


@api_view(['DELETE'])
def delete_article(request, pk):
    pass
