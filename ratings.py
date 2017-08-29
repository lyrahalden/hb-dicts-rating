"""Restaurant rating lister."""

from random import choice


def rest_rating(filename):
    """
    Returns alphabetical order of restaurant ratings
    """

    ratings = open(filename)
    rest_dict = {}

    for line in ratings:
        line = line.rstrip()
        line = line.split(":")
        rest_dict[line[0]] = line[1]

    return rest_dict

    #close(ratings)


def get_rating():
    """Gets a valid rating"""

    while True:
        new_rating = raw_input("Please enter a new rating for that restaurant. ")

        try:
            new_rating = int(new_rating)
        except ValueError:
            print "This is not an integer. Please try again."
            continue

        if new_rating > 5 or new_rating < 1:
            print "This is not a rating between 1 and 5. Please try again."
            continue

        return new_rating


def add_rating(rest_dictionary):
    """ Adds a restaurant and rating to the restaurant dictionary"""

    new_rest = raw_input("Please enter a new restaurant name. ")

    new_rating = get_rating()

    rest_dict[new_rest] = new_rating

    return rest_dict


def print_sorted_dictionary(dictionary):
    """
    prints a given dictionary sorted by alphabetical order.
    """

    alpha_rest_list = sorted(dictionary.keys())

    for rest in alpha_rest_list:
        print "%s is rated at %s." % (rest, dictionary[rest])


def update_rating(restaurant, rest_dict):
    """Update the rating for a restaurant"""

    print "The rating for %s is %s." % (restaurant, rest_dict[restaurant])

    new_rating = get_rating()

    rest_dict[restaurant] = new_rating

    return rest_dict


rest_dict = rest_rating("scores.txt")


while True:
    answer = raw_input("Enter 's' to see all the ratings" +
                        " or 'a' to add a restaurant" +
                        " or 'q' to quit " +
                        "or 'r' to update a random restaurant. ")
    if answer.lower() == "q":
        break
    elif answer.lower() == "s":
        print_sorted_dictionary(rest_dict)
    elif answer == "a":
        add_rating(rest_dict)
    elif answer == "r":
        random_restaurant = choice(rest_dict.keys()
        update_rating(random_restaurant, rest_dict)
    else:
        print "That is not a valid choice. Try again"
