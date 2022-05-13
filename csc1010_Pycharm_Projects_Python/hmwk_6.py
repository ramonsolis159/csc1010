# Ramon Montoya
# This program is for an assignment.

# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person = {'first_name': 'Ramon', 'last_name': 'Montoya', 'age': 19, 'city': 'Plano'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print()

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favorite_numbers = {'Ramon': '19', 'Ricky': '16', 'Brian': '10',
                    'Bryan': '7', 'Sabino': '22', 'Diana': '2', 'Karla': '7'}

print("Ramon's favorite number is " + favorite_numbers['Ramon'] + ".")
print("Ricky's favorite number is " + favorite_numbers['Ricky'] + ".")
print("Brian's favorite number is " + favorite_numbers['Brian'] + ".")
print("Bryan's favorite number is " + favorite_numbers['Bryan'] + ".")
print("Sabino's favorite number is " + favorite_numbers['Sabino'] + ".")
print("Diana's favorite number is " + favorite_numbers['Diana'] + ".")
print("Karla's favorite number is " + favorite_numbers['Karla'] + ".")

print()

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

python_dictionary = {
    'Class': 'A code template for creating objects.',
    'Comments': 'A code with simple descriptions that is easy for humans to read and notice for any design decisions.',
    'Dictionaries': 'Contain keys of different types for as the key acts as the value that is entered.',
    'Functions': 'Python functions can be used to abstract pieces of code to use elsewhere.',
    'Function Objects': 'They are stored in variables and lists where then they are returned by other functions.'
}

print("\nClass: " + python_dictionary['Class'])
print("\nComments: " + python_dictionary['Comments'])
print("\nDictionaries: " + python_dictionary['Dictionaries'])
print("\nFunctions: " + python_dictionary['Functions'])
print("\nFunction Objects: " + python_dictionary['Function Objects'])

print()

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

python_dictionary = {
    'Class': 'A code template for creating objects.',
    'Comments': 'A code with simple descriptions that is easy for humans to read and notice for any design decisions.',
    'Dictionaries': 'Contain keys of different types for as the key acts as the value that is entered.',
    'Functions': 'Python functions can be used to abstract pieces of code to use elsewhere.',
    'Function Objects': 'They are stored in variables and lists where then they are returned by other functions.',
    'List Comprehensions': 'Convenient ways to generate or extract information from lists.',
    'Lists': 'A data type found in Python that usually holds an ordered collection of values.',
    'For Loops': 'Python providing a clean iteration syntax.',
    'While Loops': 'A control flow statement that allows code to be repeated depending on the given condition.',
    'Sets': 'Collections of unique but unordered items.'
}

for word, meaning in python_dictionary.items():
    print("\n" + word.title() + ": " + meaning)

print("\n")

# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print()

poll_people = ['jen', 'phil', 'ricky', 'brian', 'bryan', 'sabino', 'karla', 'eli']
for people in poll_people:
    if people in sorted(favorite_languages.items()):
        print(people.title() + ", thank you for responding and taking the poll.")
    else:
        print(people.title() + ", this is a message on letting you know that you need to take the poll, thanks!")

print("\n")

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

pet_1 = {'name': 'Charlie', 'kind': 'Dog', 'gender': 'Male', 'owner': 'Oliver'}
pet_2 = {'name': 'Bella', 'kind': 'Dog', 'gender': 'Female', 'owner': 'Olivia'}
pet_3 = {'name': 'Max', 'kind': 'Cat', 'gender': 'Male', 'owner': 'Harry'}
pet_4 = {'name': 'Luna', 'kind': 'Cat', 'gender': 'Female', 'owner': 'Amelia'}
pet_5 = {'name': 'Cooper', 'kind': 'Ferret', 'gender': 'Male', 'owner': 'Jack'}
pet_6 = {'name': 'Lucy', 'kind': 'Rabbit', 'gender': 'Female', 'owner': 'Isla'}
pet_7 = {'name': 'Leo', 'kind': 'Hedgehog', 'gender': 'Male', 'owner': 'George'}
pet_8 = {'name': 'Daisy', 'kind': 'Bird', 'gender': 'Female', 'owner': 'Emily'}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6, pet_7, pet_8]
for pet in pets:
    print(pet)

print()

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers = {'Ramon': ['19', '91'], 'Ricky': ['16', '61'], 'Brian': ['10', '100', '7'],
                    'Bryan': ['7', '71', '10'], 'Sabino': ['22', '220', '96'],
                    'Diana': ['2', '4', '7'],  'Karla': ['7', '42', '71']
                    }
for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " 's favorite numbers are:")
    for number in numbers:
        print("\t" + number.title())

print()

# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output.


class User():
    """A simple attempt to model users."""

    def __init__(self, first_name, last_name, age, location):
        """Initialize the different attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        """Simulate a response to the command."""
        print(self.first_name.title() + " " + (self.last_name.title() + " is the user's full name."))
        print("The user is " + str(self.age) + " years old.")
        print("The user is from " + self.location.title() + ".")

    def greet_user(self):
        """Simulate a greeting response to the command"""
        print("Hello there " + self.first_name.title() + " " + self.last_name.title() + "! How are you today?\n")


class Admin(User):
    """Represents the special kind of user"""

    def __init__(self, first_name, last_name, age, location):
        """Initialize the different attributes"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


class Privileges():
    """List the following set of privileges"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


ramon_user = Admin('Ramon', 'Montoya', '20', 'USA')
brian_user = User('Brian', 'Morales', '19', 'USA')
karla_user = User('Karla', 'Guzman', '19', 'USA')
eli_user = User('Elizabeth', 'Nava', '19', 'USA')
sabino_user = User('Sabino', 'Mendez', '19', 'USA')

ramon_user.describe_user()
ramon_user.privileges.show_privileges()
print("\nAdding privileges...")
ramon_user_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    'can install updates',
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
ramon_user.privileges.privileges = ramon_user_privileges
ramon_user.privileges.show_privileges()
ramon_user.greet_user()

brian_user.describe_user()
brian_user.greet_user()

karla_user.describe_user()
karla_user.greet_user()

eli_user.describe_user()
eli_user.greet_user()

sabino_user.describe_user()
sabino_user.greet_user()

print()

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”
rental_car = input("\nWhat kind of a rental car would you like? ")
print("Let me see if I can find you a " + rental_car + ".")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.
table = input("\nHow many people are in your dinner group? ")
table = int(table)
if table > 8:
    print("\nYou will have to wait for a table")
else:
    print("\nPlease follow me to your table")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwich_orders = ['BLT', 'Meat ball sub', 'Turkey', 'Roast Beef', 'Ham and Cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

name_prompt = "\nWhat is your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")

# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

def display_message():
    """Display a message about what I am learning."""
    msg = "I am learning how to store code in functions."
    print(msg)


display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
    """Display a message about my favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Maze Runner')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.


def make_shirt(size, message):
    """Summarize the shirt that is going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')


make_shirt('Medium', 'FORTNITE!')
make_shirt(message="RuneScape.", size='Large')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.


def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that is going to be made."""
    print("\nI am going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'I like computer science.')

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.


def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())


city = city_country('Santiago', 'Chile')
print(city)

city = city_country('Chicago', 'USA')
print(city)

city = city_country('Paris', 'France')
print(city)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.


def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who is the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.


def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ['David Copperfield', 'Doug Henning', 'Lance Burton', 'Ricky Jay', 'Mark Wilson']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a different number
# of arguments each time.

def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")


make_sandwich('american cheese', 'white cheese', 'cheddar cheese', 'italian cheese')
make_sandwich('ham', 'bacon', 'meat balls', 'chicken', 'turkey')
make_sandwich('lettuce', 'tomatoes', 'pickles', 'black olives', 'green peppers', 'spinach')

# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly


def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict


my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

# 8-15. Printing Models: Put the functions for the example print_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of print_models.py, and modify the file to use the imported functions.

"""Functions related to printing 3d models."""


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

"""Functions related to printing 3d models."""


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)