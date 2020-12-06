from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Workout
from datetime import datetime
import re


# The function in essence renders the "overview" template in the context of all the data stored in the "Workout" table.
# That is to say it handles all the traffic to and from the home page.
def overview(request):
    context = {
        "workouts": Workout.objects.all()
    }
    return render(request, "blog/overview.html", context)  # Context allows references to be made in the HTML files.


# We used generic class-based views to create, update, and delete "posts" in the "Workout" table.


# Creates the type of view seen on the FitHub home page. That is to say a view of all the workouts of all the users who
# have registered and entered data on the platform. It is the same regardless of whether a user is signed in or of which
# user is signed in.
class PostListView(ListView):
    model = Workout  # Specifies which model should be queried when generating the list of workouts to display.
    template_name = 'blog/overview.html'  # Specifies the template that should be used to display the queried info.
    context_object_name = 'workouts'  # Specifies the object list that should be iterated over.
    ordering = ['-date']  # Specifies the order in which the workouts are sorted.
    paginate_by = 5  # Limits how many workouts are displayed on each page.


# Creates a list of all the workouts a specific user has entered. It is the type of list a user views when they click
# on a specific user's username.
class UserPostListView(ListView):
    model = Workout
    template_name = 'blog/user_posts.html'
    context_object_name = 'workouts'
    paginate_by = 5

    # This function allows us to dynamically filter the list of workouts shown on the site accordingly to which
    # username was clicked on.
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Workout.objects.filter(athlete=user).order_by('-date')


# This is the view used when a user is interested in all of the details of a specific workout.
class PostDetailView(DetailView):
    model = Workout


# This is the view a user encounters when they wish to enter a workout view the "Add Workout" form. Note that a user is
# required to be logged into the site.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Workout

    # Specifies which fields should be shown to the user in the form. We as the designers of the application have the
    # option of restricting which fields are shown, but given the application context, it did not make sense to do so.
    fields = ['title', 'description', 'date', 'start_time', 'end_time', 'sport', 'type', 'distance', 'workout_intensity']

    # This functions validates the form again. The original validation needs to be overridden since we changed the form
    # instance.
    def form_valid(self, form):
        form.instance.athlete = self.request.user
        return super().form_valid(form)


# This is the view a user encounters when they wish to update a workout they previously entered. Note that a user is
# required to be logged into the site and that they can only update one of their own workouts.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout

    # Specifies which fields the user should be able to update.
    fields = ['title', 'description', 'date', 'start_time', 'end_time','sport', 'type', 'distance', 'workout_intensity']

    # This functions validates the form again. The original validation needs to be overridden since we changed the form
    # instance.
    def form_valid(self, form):
        form.instance.athlete = self.request.user
        return super().form_valid(form)

    # This function ensures that the user currently signed into the site is the same as the one who originally entered
    # the workout in the first place.
    def test_func(self):
        workout = self.get_object()
        if self.request.user == workout.athlete:
            return True
        return False


# This is the view a user encounters when they wish to delete a workout they previously entered. Note that a user is
# required to be logged into the site and that they can only delete one of their own workouts.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout
    success_url = '/'  # Defines the success criteria to know that the function executed successfully.

    # This function ensures that the user currently signed into the site is the same as the one who originally entered
    # the workout in the first place.
    def test_func(self):
        workout = self.get_object()
        if self.request.user == workout.athlete:
            return True
        return False


# This function renders what a user views on the "Workout Analysis" tab.
def analysis(request):
    xAxisID = []
    yAxisID = []
    time = []
    time2 = []
    time3 = []
    speedid = []
    current_user = request.user
    queryset = Workout.objects.order_by('-date')
    for workout in queryset:  # Adds the data
        if current_user == workout.athlete:
            yAxisID.append(workout.distance)
            xAxisID.append(workout.date)
            time.append(workout.start_time)
            time2.append(workout.end_time)
    if yAxisID:
        for i in range(len(yAxisID)):
            yAxisID[i] = float(yAxisID[i])  # Float data type for kilometers
            time[i] = str(time[i])
            time[i] = re.sub('\+00:00', '', time[i])  # Regular expressions
            time2[i] = str(time2[i])
            time2[i] = re.sub('\+00:00', '', time2[i])   
            time[i] = datetime.strptime(time[i],"%Y-%m-%d %H:%M:%S")
            time2[i] = datetime.strptime(time2[i],"%Y-%m-%d %H:%M:%S")
            
        for i in range(len(time2)):  # Computes duration. This way end time cannot be earlier than start time.
            time3.append(time2[i]-time[i])

        for i in range(len(time3)):
            time3[i] = float(time3[i].total_seconds()/60)
            
        for i in range(len(xAxisID)):
            xAxisID[i] = str(xAxisID[i])
            xAxisID[i] = xAxisID[i].split(' ')[0]

        i = 1

        while i != len(xAxisID):  # Sums the duration of workouts that occur on the same day.
            if xAxisID[i] == xAxisID[i-1]:
                yAxisID[i-1] = yAxisID[i]+yAxisID[i-1]
                time3[i-1] = time3[i]+time3[i-1]
                xAxisID.pop(i)
                yAxisID.pop(i)
                time3.pop(i)
                i = i-1
            i = i+1

        if len(yAxisID) > 7:  # Keeps the last seven days of workout data.
            for x in range(len(yAxisID)):
                if len(yAxisID) > 7:
                    xAxisID.pop(-1)
                    yAxisID.pop(-1)
                    time3.pop(-1)

        for i in range(len(time3)):  # Calculates the speed of the workout.
            speedid.append((time3[i]/yAxisID[i]))

        for i in range(len(speedid)):
            speedid[i] = str(round(speedid[i], 2))

        return render(request, "blog/analysis.html", {
            'title': 'Workout Analysis',
            'labels': xAxisID,
            'data': yAxisID,
            'speed': speedid,
            'error': False
        })
    else:
        return render(request, "blog/analysis.html", {  # Returns what we need for the graphs in analysis.html.
                'title': 'Workout Analysis',
                'error': True
        })
  

def bests(request):
    return render(request, "blog/bests.html", {"title": "Personal Bests"})
