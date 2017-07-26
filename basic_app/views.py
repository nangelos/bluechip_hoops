from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfo, RecruitProfileInfoForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def info(request):
    return render(request, 'basic_app/info.html')

def register(request):
    # registered = False
    # if request.method == "POST":
    #     user_form = UserForm(data = request.POST)
    #     if user_form.is_valid():
    #         user = user_form.save()
    #         create = User.objects.create()
    #         create.email = user.email
    #         create.password = user.password
    #         create.username = user.email
    #         create.save()
    #         # user.set_password(user.password)
    #         # user.save()
    #         registered = True
    # else:
    #     user_form = UserForm()
    #     profile_form = UserProfileInfo()
    # return render(request, 'basic_app/signup.html', {'user_form':user_form, 'registered':registered, 'profile_form':profile_form})

    registered=False
    if request.method =='POST':
        user_form =UserForm(data=request.POST)
        profile_form=UserProfileInfo(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfo()

    return render(request,'basic_app/signup.html',
            {'user_form':user_form,'profile_form':profile_form,
            'registered':registered})

def news(request):
    return render(request, 'basic_app/news.html')

def natl_rank(request):
    return render(request, 'basic_app/natl_ranks.html')

def my_recruits(request):
    return render(request, "basic_app/my_recruits.html")

def upcoming(request):
    return render(request, "basic_app/upcoming.html")

def manage_staff(request):
    return render(request, "basic_app/staff.html")

def manage_social(request):
    return render(request, "basic_app/social.html")

# def user_logout(request):
#     # Log out the user.
#     logout(request)
#     # Return to homepage.
#     return HttpResponseRedirect(reverse('index'))

# def register(request):
#
#     registered = False
#
#     if request.method == 'POST':
#
#         # Get info from "both" forms
#         # It appears as one form to the user on the .html page
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileInfoForm(data=request.POST)
#
#         # Check to see both forms are valid
#         if user_form.is_valid() and profile_form.is_valid():
#
#             # Save User Form to Database
#             user = user_form.save()
#
#             # Hash the password
#             user.set_password(user.password)
#
#             # Update with Hashed password
#             user.save()
#
#             # Now we deal with the extra info!
#
#             # Can't commit yet because we still need to manipulate
#             profile = profile_form.save(commit=False)
#
#             # Set One to One relationship between
#             # UserForm and UserProfileInfoForm
#             profile.user = user
#
#             # Check if they provided a profile picture
#             if 'profile_pic' in request.FILES:
#                 print('found it')
#                 # If yes, then grab it from the POST form reply
#                 profile.profile_pic = request.FILES['profile_pic']
#
#             # Now save model
#             profile.save()
#
#             # Registration Successful!
#             registered = True
#
#         else:
#             # One of the forms was invalid if this else gets called.
#             print(user_form.errors,profile_form.errors)
#
#     else:
#         # Was not an HTTP post so we just render the forms as blank.
#         user_form = UserForm()
#         profile_form = UserProfileInfoForm()
#
#     # This is the render and context dictionary to feed
#     # back to the registration.html file page.
#     return render(request,'basic_app/signup.html',
#                           {'user_form':user_form,
#                            'profile_form':profile_form,
#                            'registered':registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('basic_app:news'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html')
