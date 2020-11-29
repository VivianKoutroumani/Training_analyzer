from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post, Workout
from datetime import datetime
import matplotlib.pyplot as plt, mpld3
import re


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
    time= []
    time2 = []
    time3=[]
    speedid= []
    current_user=request.user
    queryset=Workout.objects.order_by('-date')
    for workout in queryset:
        if current_user==workout.athlete: 
            yAxisID.append(workout.distance)
            xAxisID.append(workout.date)
            time.append(workout.start_time)
            time2.append(workout.end_time)
        
    for i in range(len(yAxisID)):
        yAxisID[i]=float(yAxisID[i])
        time[i]=str(time[i])
        time[i] = re.sub('\+00:00', '', time[i])
        time2[i]=str(time2[i])
        time2[i] = re.sub('\+00:00', '', time2[i])   
        time[i]=datetime.strptime(time[i],"%Y-%m-%d %H:%M:%S")
        time2[i]=datetime.strptime(time2[i],"%Y-%m-%d %H:%M:%S")
        
    for i in range(len(time2)):
        time3.append(time2[i]-time[i])

    for i in range(len(time3)):
        time3[i]=float(time3[i].total_seconds()/60)
           
    for i in range(len(xAxisID)):
        xAxisID[i]=str(xAxisID[i])
        xAxisID[i]=xAxisID[i].split(' ')[0]
    i=1
   # print("test2")
    #if len(xAxisID)>1:
    #   
    while i!=len(xAxisID):
        if xAxisID[i]==xAxisID[i-1]:
            print("test")
            yAxisID[i-1]=yAxisID[i]+yAxisID[i-1]
            time3[i-1]=time3[i]+time3[i-1]
            xAxisID.pop(i)
            yAxisID.pop(i)
            time3.pop(i)
            i=i-1
        i=i+1
    if len(yAxisID) > 7:
        for x in range(len(yAxisID)):
            if len(yAxisID) > 7:
                 xAxisID.pop(-1)
                 yAxisID.pop(-1)
                 time3.pop(-1)
    for i in range(len(time3)):
        speedid.append((yAxisID[i]/time3[i]))
    for i in range(len(speedid)):
        speedid[i]=str(round(speedid[i], 2))


    return render(request, "blog/analysis.html", {
        'title': 'Workout Analysis',
        'labels': xAxisID,
        'data': yAxisID,
        'speed' : speedid,
    })
  #queryset = Workout.objects.order_by('-date')[]
    #for Workout in queryset:
      #  labels.append(Workout.date)
       # data.append(city.population)

    
 
def bests(request):
    return render(request, "blog/bests.html", {"title": "Personal Bests"})
