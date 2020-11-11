from django.urls import path
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView, 
	PostDeleteView,
	UserPostListView
	)
from . import views

urlpatterns = [
	path("",PostListView.as_view(), name="blog-overview"), ## .as_view converts in actual view
	path("user/<str:username>",UserPostListView.as_view(), name="user-posts"),
	path("post/<int:pk>/",PostDetailView.as_view(), name="post-detail"), # pk = primarykey
	path("post/new/",PostCreateView.as_view(), name="post-create"),
	path("post/<int:pk>/update/",PostUpdateView.as_view(), name="post-update"),
	path("post/<int:pk>/delete/",PostDeleteView.as_view(), name="post-delete"),
	path("trainingAnalysis/",views.trainingAnalysis, name="blog-trainingAnalysis"),
	path("personalBest/",views.personalBest, name="blog-personalBest"),
]

# <app|/<model><viewtype>.html -> thats where it looks for
