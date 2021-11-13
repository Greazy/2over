from django.urls import path
from .import views


urlpatterns = [
    path('', views.get_all_articles, name='get_user_articles'),
    path('<int:pk>/detail/', views.get_article, name='get_article'),
    path('<int:pk>/update/', views.update_article, name='update_article'),
    path('<int:pk>/delete', views.delete_article, name='delete_article'),
    path('create/', views.create_article, name='create_article')
]