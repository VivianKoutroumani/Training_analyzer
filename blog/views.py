from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post, Workout
import matplotlib.pyplot as plt, mpld3


def overview(request):
    context = {
        "workouts": Workout.objects.all()
    }
    return render(request, "blog/overview.html", context)


class PostListView(ListView):
    model = Workout  # What model to query to create list
    template_name = 'blog/overview.html'  # <app>/<model>_<viewtype>.html -> thats where it looks for by default
    context_object_name = 'workouts'  # normally it would look after "object list" by default to loop over so we have to rename it
    ordering = ['-date']  # - goes from newest to oldest; without it goes from oldest to newest
    paginate_by = 5


class UserPostListView(ListView):
    model = Workout
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html -> thats where it looks for by default
    context_object_name = 'workouts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Workout.objects.filter(athlete=user).order_by('-date')


class PostDetailView(DetailView):
    model = Workout


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['title', 'description', 'date', 'start_time', 'end_time','sport', 'type', 'distance', 'workout_intensity']

    def form_valid(self, form):
        form.instance.athlete = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    fields = ['title', 'description', 'date', 'start_time', 'end_time','sport', 'type', 'distance', 'workout_intensity']

    def form_valid(self, form):
        form.instance.athlete = self.request.user
        return super().form_valid(form)

    def test_func(self):
        workout = self.get_object()
        if self.request.user == workout.athlete:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout
    success_url = '/'

    def test_func(self):
        workout = self.get_object()
        if self.request.user == workout.athlete:
            return True
        return False


def analysis(request):
    xAxisID= []
    yAxisID = []
    current_user=request.user
    queryset=Workout.objects.order_by('-date')
    for workout in queryset:
        if current_user==workout.athlete: 
            yAxisID.append(workout.distance)
            xAxisID.append(workout.date)
    for i in range(0, len(yAxisID)):
        yAxisID[i]=float(yAxisID[i])
    for i in range(0, len(xAxisID)):
        xAxisID[i]=str(xAxisID[i])
        xAxisID[i]=xAxisID[i].split(' ')[0]
    if len(yAxisID) > 7:
        for x in range(7,len(yAxisID)):
            if len(yAxisID) > 7:
                 xAxisID.pop(-1)
                 yAxisID.pop(-1)

    return render(request, "blog/analysis.html", {
        'title': 'Workout Analysis',
        'labels': xAxisID,
        'data': yAxisID,
    })

  #queryset = Workout.objects.order_by('-date')[]
    #for Workout in queryset:
      #  labels.append(Workout.date)
       # data.append(city.population)

    
 
def bests(request):
    return render(request, "blog/bests.html", {"title": "Personal Bests"})
