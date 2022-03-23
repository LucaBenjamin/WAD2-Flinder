import django.http
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect
# Temp
import urllib.request
import json

# Create your views here.
def index(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/index.html", context=context_dict)

    return response


def login(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/login.html", context=context_dict)

    return response


def register(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/register.html", context=context_dict)

    return response


@login_required
def register_account_type(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/register_account_type.html", context=context_dict)

    return response


@login_required
def register_room_seeker(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/register_room_seeker.html", context=context_dict)

    return response


@login_required
def register_room_provider(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/register_room_provider.html", context=context_dict)

    return response


@login_required
def upload_photos(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/upload_photos.html", context=context_dict)

    return response


@login_required
def edit_profile(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/edit_profile.html", context=context_dict)

    return response


@login_required
def main(request):
    # Query the database for any data needed to build the page

    # Context for the html template
    context_dict = {

    }

    # Render the web page
    response = render(request, "flinder/main.html", context=context_dict)

    return response


@login_required
def profile(request, profile_slug):
    # Query the database for any data needed to build the page
    # TODO: Once the model is complete, import it and uncomment this code
    # try:
    #    profile = Profile.objects.get(slug=profile_slug)
    # except Profile.DoesNotExist:
    #    profile = None
    # TODO: Remove
    db_profile = None

    # If the profile doesn't exist, redirect the user to the main page
    if db_profile is None:
        return redirect('flinder:main')

    # Context for the html template
    context_dict = {
        "profile": db_profile,
    }

    # Render the web page
    response = render(request, "flinder/profile.html", context=context_dict)

    return response


@login_required
def get_matches(request):
    # Check that this is an API call
    if request.accepts('text/html'):
        return HttpResponseNotAllowed(permitted_methods=["GET"])

    # Get the user asking for matches
    user = request.user
    # TODO: Call the matching algorithm to get the data here
    matches = json.loads(urllib.request.urlopen("https://api.mockaroo.com/api/7e1549e0?count=10&key=6bc6a940"))

    return JsonResponse(matches)
