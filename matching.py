from flinderserver.models import UserProfile, Pictures, InterestsAndPriorities, Swipe;
#More comparisons to be done
def get_compatability(user1, user2):
    compatability = 0;
    user1_interests = user1.interests;
    user2_interests = user2.interests;

    if not user1.mixedYearOfStudy and user1.yearOfStudy != user2.yearOfStudy:
        return -1000;

    if user1_interests.pets and user2_interests.pets:
        compatability += 10;
    else:
        compatability -= 10;
    if user1_interests.food and user2_interests.food:
        compatability += 3;
    else:
        compatability -= 3;
    if user1_interests.sports and user2_interests.sports:
        compatability += 2;
    else:
        compatability -= 2;
    if user1_interests.music and user2_interests.sports:
        compatability += 5;
    else:
        compatability -= 5;
    if user1_interests.partying and user2_interests.partying:
        compatability += 12;
    else:
        compatability -= 12;
    if user1_interests.drinking and user2_interests.drinking:
        compatability += 7;
    else:
        compatability -= 7;
    if user1_interests.drinking and user2_interests.drinking:
        compatability += 7;
    else:
        compatability -= 7;
    if user1_interests.strictQuietHours and user2_interests.strictQuietHours:
        compatability += 15;
    else:
        compatability -= 15;
