from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from all_apps.users.models import *
from django.views import View
from all_apps.users.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile, Stats
from datetime import date
from all_apps.assignments.models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def sign_up(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        user_email = request.POST.get('email-id')
        user_first_name = request.POST.get('first-name')
        user_pass2 = request.POST.get('confirm-password')

        # Simple validation: Ensure passwords match
        

        # Ensure email and username are provided
        if not user_name or not user_email:
            return HttpResponse("Missing username or email", status=400)

        try:
            # Create a new user
            user = User.objects.create_user(
                username=user_name,
                email=user_email,
                first_name=user_first_name,
                password=user_pass2
            )
            user.save()

            # Authenticate and log in the user
            auth = authenticate(username=user_name, password=user_pass2)
            if auth is not None:
                login(request, auth)
                return redirect("all-assignment")
            else:
                return HttpResponse("Authentication failed", status=401)
        except Exception as e:
            return HttpResponse(f"Error occurred: {str(e)}", status=500)
    else:
        return HttpResponse("Invalid request method", status=405)


def sign_in(request):
    if request.method=="POST":
        user=request.POST.get('username')
        pass1=request.POST.get('password')
        auth=authenticate(username=user,password=pass1)
        if auth is not None:
            login(request,auth)
            return redirect('all-assignment')
        else:
            return HttpResponse("Registration failed", status=401)
    return render(request,'login.html')


@login_required  # Ensures the user is logged in
def profile(request):
    try:
        # Fetch the profile for the currently logged-in user
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # In case the profile does not exist

    context = {'profile': profile}
    return render(request, 'profile.html', context)




class ProfileUpdateView(View):
    def get(self, request, pk):
        # Fetch profile by primary key (pk)
        profile = get_object_or_404(Profile, pk=pk)
        # Initialize form with the profile instance
        form = ProfileForm(instance=profile)
        return render(request, 'profile_update.html', {'form': form, 'profile': profile})

    def post(self, request, pk):
        # Fetch profile by primary key (pk)
        profile = get_object_or_404(Profile, pk=pk)
        # Initialize form with POST and FILES data
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        print("Form Data:", request.POST)  # Print POST data
        print("Form Files:", request.FILES)  # Print FILES data
        print("Form is valid:", form.is_valid())  # Check if the form is valid

        if form.is_valid():
            form.save()  # Save the form data
            print("Form saved successfully.")
            return redirect('profile')  # Redirect to profile after saving
        else:
            # If form is not valid, print errors
            print("Form errors:", form.errors)

        return render(request, 'profile_update.html', {'form': form, 'profile': profile})

def user_logout(request):
    logout(request)
    return redirect('sign-in')




def stats(request):
    if request.method == "POST":
       
        topic_name = request.POST.get('topic_name')
        assignment_id = request.POST.get('assignment_id')
        topic_id = request.POST.get('topic_id')

        try:
            topic = AssignmentTopic.objects.get(id=topic_id)
        except AssignmentTopic.DoesNotExist:
            return HttpResponse("Topic not found.", status=404)


        user_profile = request.user.profile  
        user_stats, created = Stats.objects.get_or_create(profile=user_profile)

        
        if user_stats.topic_names:
            user_stats.topic_names += f", {topic_name}"
        else:
            user_stats.topic_names = topic_name

        user_stats.total_downloads += 1
        user_stats.save()
        return redirect(topic.pdf.url)
    # If it's a GET request, render a stats page
    return render(request, 'alls.html')



def view_stats(request):
    # Assuming you're getting the current user's stats
    stats = Stats.objects.get(profile__user=request.user)
    return render(request, 'stats.html', {'stats': stats})
