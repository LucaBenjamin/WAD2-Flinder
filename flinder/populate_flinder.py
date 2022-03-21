#!/usr/bin/env python
import os

import django

from Data import Get_data

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flinder.settings')
django.setup()
from flinderserver.models import UserProfile, Pictures, Preferences, InterestsAndPriorities, Swipe

from django.contrib.auth.models import User


def populate():
    users = Get_data()
    for data in users:
        user = add_user(data["user"])
        data["user_profile"]["user"] = user
        add_user_profile(data["user_profile"], user)
        data["preferences"]["user"] = user
        add_preferences(data["preferences"])
        data["interestsAndPriorities"]["user"] = user
        add_interests_and_priorities(data["interestsAndPriorities"])
        data["picture"]["user"] = user
        add_picture(data["picture"])


def add_swipe(swipe):
    new_swipe = Swipe.objects.get_or_create(swiped_id=swipe["swiped"].user_id, swiper_id=swipe["swiper"].user_id,
                                            swipeRight=swipe["swipeRight"])[0]
    new_swipe.swiper_id = swipe["swiper"]
    new_swipe.swiped_id = swipe["swiped"]
    new_swipe.swipeRight = swipe["swipeRight"]
    new_swipe.save()
    return new_swipe


def add_preferences(preferences):
    new_preferences = \
        Preferences.objects.get_or_create(poster_id=preferences["user"].id, mixedGender=preferences["mixedGender"],
                                          mixedYearOfStudy=preferences["mixedYearOfStudy"]
                                          , mixedAge=preferences["mixedAge"],
                                          )[0]
    new_preferences.posterId = preferences["user"].id
    new_preferences.mixedGender = preferences["mixedGender"]
    new_preferences.mixedAge = preferences["mixedAge"]
    new_preferences.mixedYearOfStudy = preferences["mixedYearOfStudy"]
    new_preferences.save()
    return new_preferences


def add_interests_and_priorities(interestsAndPriorities):
    new_interestsAndPriorities = \
        InterestsAndPriorities.objects.get_or_create(poster_id=interestsAndPriorities["user"].id
                                                     , pets=interestsAndPriorities["pets"]
                                                     , food=interestsAndPriorities["food"]
                                                     , sports=interestsAndPriorities["sports"]
                                                     , music=interestsAndPriorities["music"]
                                                     , partying=interestsAndPriorities["partying"]
                                                     , drinking=interestsAndPriorities["drinking"]
                                                     , flatCleanliness=interestsAndPriorities["flatCleanliness"]
                                                     , strictQuietHours=interestsAndPriorities["strictQuietHours"])[0]
    new_interestsAndPriorities.poster_id = interestsAndPriorities["user"].id
    new_interestsAndPriorities.pets = interestsAndPriorities["pets"]
    new_interestsAndPriorities.food = interestsAndPriorities["food"]
    new_interestsAndPriorities.sports = interestsAndPriorities["sports"]
    new_interestsAndPriorities.music = interestsAndPriorities["music"]
    new_interestsAndPriorities.partying = interestsAndPriorities["partying"]
    new_interestsAndPriorities.drinking = interestsAndPriorities["drinking"]
    new_interestsAndPriorities.flatCleanliness = interestsAndPriorities["flatCleanliness"]
    new_interestsAndPriorities.strictQuietHours = interestsAndPriorities["strictQuietHours"]
    new_interestsAndPriorities.save()
    return new_interestsAndPriorities


def add_picture(picture):
    new_picture = Pictures.objects.get_or_create(poster_id=picture["user"].id)[0]
    new_picture.poster_id = picture["user"]
    new_picture.picture = picture["picture"]
    new_picture.description = picture["description"]
    new_picture.save()
    return new_picture


def add_user(user):
    user = User.objects.get_or_create(username=user["userName"], email=user["email"])[0]
    user.save()
    return user


def add_user_profile(user_profile, OriginalUser):
    new_user = UserProfile()
    new_user.name = user_profile["name"]
    new_user.emailAddress = OriginalUser
    new_user.dateOfBirth = user_profile["dateOfBirth"]
    new_user.flatSearcher = user_profile["flatSearcher"]
    new_user.gender = user_profile["gender"]
    new_user.yearOfStudy = user_profile["yearOfStudy"]
    new_user.flatBedrooms = user_profile["flatBedrooms"]
    new_user.freeBedrooms = user_profile["freeBedrooms"]
    new_user.university = user_profile["university"]
    new_user.postCode = user_profile["postCode"]
    new_user.mixedYearOfBirth = user_profile["mixedYearOfBirth"]
    new_user.addressLine1 = user_profile["addressLine1"]
    new_user.addressLine2 = user_profile["addressLine2"]
    print(user_profile["name"])
    new_user.save()
    return new_user


if __name__ == '__main__':
    print('Starting flinder population script...')
    populate()