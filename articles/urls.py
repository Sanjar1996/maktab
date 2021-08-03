from django.urls import path
from .views import BlogListView, BlogDeleteView, BlogUpdateView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog-edit'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('new/', BlogCreateView.as_view(), name='blog-new')
]