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


# This file creates all the links which allow users to travel from page to page within the FitHub platform. In other
# words, it maps URLs to each view function. What appears inside the double quotation marks after "path(" is what
# appears in the URL that's displayed in the user's web browser when they are on any given page.


urlpatterns = [

	# The ".as_view" suffix converts each link to the actual view, which is listed at the end of each line.
	path("",PostListView.as_view(), name="blog-overview"),
	path("user/<str:username>",UserPostListView.as_view(), name="user-posts"),
	path("post/<int:pk>/",PostDetailView.as_view(), name="workout-detail"),  # "pk" means primary key.
	path("post/new/",PostCreateView.as_view(), name="post-create"),
	path("post/<int:pk>/update/",PostUpdateView.as_view(), name="post-update"),
	path("post/<int:pk>/delete/",PostDeleteView.as_view(), name="post-delete"),
	path("analysis/",views.analysis, name="blog-analysis"),
	path("bests/",views.bests, name="blog-bests"),
]

