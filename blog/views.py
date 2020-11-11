from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post

def overview(request):
	context = {
		"posts": Post.objects.all()
	}
	return render(request, "blog/overivew.html",context)

class PostListView(ListView):
	model = Post # What model to query to create list
	template_name = 'blog/overview.html' # <app>/<model>_<viewtype>.html -> thats where it looks for by default
	context_object_name = 'posts' # normally it would look after "object list" by default to loop over so we have to rename it
	ordering = ['-date_posted'] # - goes from newest to oldest; without it goes from oldest to newest
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html -> thats where it looks for by default
	context_object_name = 'posts' 
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)	

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)	

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def trainingAnalysis(request):
	return render(request, "blog/trainingAnalysis.html", {"title": "Training Analysis"})

def personalBest(request):
	return render(request, "blog/personalBest.html", {"title": "Personal Best"})



# Create your views here.
