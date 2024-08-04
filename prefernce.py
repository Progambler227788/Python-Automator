import random

# Part a: Function to Create Preference Lists
def create_preference_lists(n):
    # Generate preference lists for men and women
    men_preferences = {f'm{i}': list(range(1, n+1)) for i in range(1, n+1)}
    women_preferences = {f'w{i}': list(range(1, n+1)) for i in range(1, n+1)}
    for prefs in men_preferences.values():
        random.shuffle(prefs)
    for prefs in women_preferences.values():
        random.shuffle(prefs)
    return men_preferences, women_preferences


# Part b: Function to Check for Unstable Pairs
def is_unstable(marriages, men_preferences, women_preferences):
    for man, woman in marriages.items():
        # Get the preference lists of the man and woman involved
        pref_list = men_preferences[man]
        woman_pref_list = women_preferences[woman]
        # Check if the current pairing is unstable
        if pref_list.index(woman) > pref_list.index(marriages[woman]) and woman_pref_list.index(man) > woman_pref_list.index(marriages[man]):
            return True
    return False

# Part c: Implementing Gale-Shapley Algorithm
def gale_shapley(men_preferences, women_preferences):
    unengaged_men = list(men_preferences.keys())
    engagements = {}
    while unengaged_men:
        man = unengaged_men.pop(0)
        woman = men_preferences[man].pop(0)
        fiance = engagements.get(woman)
        if not fiance:
            engagements[woman] = man
        else:
            woman_pref_list = women_preferences[woman]
            if woman_pref_list.index(man) < woman_pref_list.index(fiance):
                engagements[woman] = man
                unengaged_men.append(fiance)
            else:
                unengaged_men.append(man)
    return engagements

import time

# Part d: Running the Algorithm 5 Times for n = 10
n = 10
times = []
for _ in range(5):
    men_preferences, women_preferences = create_preference_lists(n)
    start_time = time.time()
    marriages = gale_shapley(men_preferences, women_preferences)
    end_time = time.time()
    times.append(end_time - start_time)
print("Average Running Time:", sum(times) / len(times))
