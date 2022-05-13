# Ramon Montoya
# This program is for an assignment.

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.


class Restaurant():
    """A simple attempt to model a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurants name and cuisine."""
        print(self.name.title() + " is now open")
        """Describes the type of cuisine"""
        print(self.type.title() + " rolled over!")


my_restaurant = Restaurant('Popeyes', 'fried chicken')
print(my_restaurant.name)
print(my_restaurant.type)
my_restaurant.describe_restaurant()
print("My restaurants's cuisine is " + my_restaurant.type.title() + ".\n")


# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.


class Restaurant():
    """A simple attempt to model a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurants name and cuisine."""
        print(self.name.title() + " is now open")
        """Describes the type of cuisine"""
        print(self.type.title() + " rolled over!")


my_restaurant = Restaurant('Popeyes', 'fried chicken')
mex_restaurant = Restaurant('Los Comales', 'torta de milanesa')
ramon_restaurant = Restaurant('El Monchis', 'enchiladas')
print(my_restaurant.name)
print(my_restaurant.type)
my_restaurant.describe_restaurant()
print("My restaurants's cuisine is " + my_restaurant.type.title() + ".\n")
print(mex_restaurant.name)
print(mex_restaurant.type)
mex_restaurant.describe_restaurant()
print("My restaurants's cuisine is " + mex_restaurant.type.title() + ".\n")
print(ramon_restaurant.name)
print(ramon_restaurant.type)
ramon_restaurant.describe_restaurant()
print("My restaurants's cuisine is " + ramon_restaurant.type.title() + ".\n")


# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.


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


ramon_user = User('Ramon', 'Montoya', '20', 'USA')
brian_user = User('Brian', 'Morales', '19', 'USA')
karla_user = User('Karla', 'Guzman', '19', 'USA')
eli_user = User('Elizabeth', 'Nava', '19', 'USA')
sabino_user = User('Sabino', 'Mendez', '19', 'USA')

ramon_user.describe_user()
ramon_user.greet_user()

brian_user.describe_user()
brian_user.greet_user()

karla_user.describe_user()
karla_user.greet_user()

eli_user.describe_user()
eli_user.greet_user()

sabino_user.describe_user()
sabino_user.greet_user()


# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.


class Restaurant():
    """A simple attempt to model a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurants name and cuisine."""
        print(self.name.title() + " is now open")
        """Describes the type of cuisine"""
        print(self.type.title() + " rolled over!")

    def set_number_served(self):
        print("This restaurant has served " + str(self.number_served) + " customers.")

    def increment_number_served(self, people):
        self.number_served += people
        print("This restaurant has served " + str(self.number_served) + " customers.")


my_restaurant = Restaurant('Popeyes', 'fried chicken')
print(my_restaurant.name)
print(my_restaurant.type)
my_restaurant.describe_restaurant()
print("My restaurants's cuisine is " + my_restaurant.type.title() + ".")
my_restaurant.set_number_served()
my_restaurant.increment_number_served(23)
my_restaurant.increment_number_served(11)
print("")


# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User():
    """A simple attempt to model users."""

    def __init__(self, first_name, last_name, age, location):
        """Initialize the different attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Simulate a response to the command."""
        print(self.first_name.title() + " " + (self.last_name.title() + " is the user's full name."))
        print("The user is " + str(self.age) + " years old.")
        print("The user is from " + self.location.title() + ".")

    def greet_user(self):
        """Simulate a greeting response to the command"""
        print("Hello there " + self.first_name.title() + " " + self.last_name.title() + "! How are you today?\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


ramon_user = User('Ramon', 'Montoya', '20', 'USA')
brian_user = User('Brian', 'Morales', '19', 'USA')
karla_user = User('Karla', 'Guzman', '19', 'USA')
eli_user = User('Elizabeth', 'Nava', '19', 'USA')
sabino_user = User('Sabino', 'Mendez', '19', 'USA')

ramon_user.describe_user()
ramon_user.greet_user()
print("Making 3 login attempts...")
ramon_user.increment_login_attempts()
ramon_user.increment_login_attempts()
ramon_user.increment_login_attempts()
print("     Login attempts: " + str(ramon_user.login_attempts))
print("Resetting login attempts...")
ramon_user.reset_login_attempts()
print("     Login attempts: " + str(ramon_user.login_attempts))
print("")

brian_user.describe_user()
brian_user.greet_user()
print("Making 3 login attempts...")
brian_user.increment_login_attempts()
brian_user.increment_login_attempts()
brian_user.increment_login_attempts()
print("     Login attempts: " + str(brian_user.login_attempts))
print("Resetting login attempts...")
brian_user.reset_login_attempts()
print("     Login attempts: " + str(brian_user.login_attempts))
print("")

karla_user.describe_user()
karla_user.greet_user()
print("Making 3 login attempts...")
karla_user.increment_login_attempts()
karla_user.increment_login_attempts()
karla_user.increment_login_attempts()
print("     Login attempts: " + str(karla_user.login_attempts))
print("Resetting login attempts...")
karla_user.reset_login_attempts()
print("     Login attempts: " + str(karla_user.login_attempts))
print("")

eli_user.describe_user()
eli_user.greet_user()
print("Making 3 login attempts...")
eli_user.increment_login_attempts()
eli_user.increment_login_attempts()
eli_user.increment_login_attempts()
print("     Login attempts: " + str(eli_user.login_attempts))
print("Resetting login attempts...")
eli_user.reset_login_attempts()
print("     Login attempts: " + str(eli_user.login_attempts))
print("")

sabino_user.describe_user()
sabino_user.greet_user()
print("Making 3 login attempts...")
sabino_user.increment_login_attempts()
sabino_user.increment_login_attempts()
sabino_user.increment_login_attempts()
print("     Login attempts: " + str(sabino_user.login_attempts))
print("Resetting login attempts...")
sabino_user.reset_login_attempts()
print("     Login attempts: " + str(sabino_user.login_attempts))
print("")


# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.


class Restaurant():
    """A simple attempt to model a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurants name and cuisine."""
        print(self.name.title() + " is now open")
        """Describes the type of cuisine"""
        print(self.type.title() + " rolled over!")


class IceCreamStand(Restaurant):
    """Represent an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize an ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


cone = IceCreamStand('Dairy Queen')
cone.flavors = ['vanilla', 'chocolate', 'black cherry', 'strawberry', 'mint']
cone.describe_restaurant()
cone.show_flavors()
print("")


# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.


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
        self.privileges = []

    def show_privileges(self):
        """List the admin's set of privileges"""
        print("Privileges:")
        for privilege in self.privileges:
            print("- " + privilege)


ramon_user = Admin('Ramon', 'Montoya', '20', 'USA')
brian_user = User('Brian', 'Morales', '19', 'USA')
karla_user = User('Karla', 'Guzman', '19', 'USA')
eli_user = User('Elizabeth', 'Nava', '19', 'USA')
sabino_user = User('Sabino', 'Mendez', '19', 'USA')

ramon_user.describe_user()
ramon_user.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    'can install updates',
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
ramon_user.show_privileges()
ramon_user.greet_user()

brian_user.describe_user()
brian_user.greet_user()

karla_user.describe_user()
karla_user.greet_user()

eli_user.describe_user()
eli_user.greet_user()

sabino_user.describe_user()
sabino_user.greet_user()


# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.


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


# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant. Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is working
# properly

from restaurant import Restaurant

greek_isle = Restaurant('the greek restaurant', 'lamb and fish')
greek_isle.describe_restaurant()
print("")

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
# Store the classes User, Privileges, and Admin in one module. Create a separate
# file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly

from user import Admin

ramon_user = Admin('Ramon', 'Montoya', '20', 'USA')
ramon_user.describe_user()

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

print("\nThe admin " + ramon_user.first_name + " has these privileges: ")
ramon_user.privileges.show_privileges()

# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

from admin import Admin

ramon_user = Admin('Ramon', 'Montoya', '20', 'USA')
ramon_user.describe_user()

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

print("\n The admin " + ramon_user.first_name + " has these privileges: ")
ramon_user.privileges.show_privileges()

# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary

from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

# 9-14. Dice: The module random contains functions that generate random numbers
# in a variety of ways. The function randint() returns an integer in the
# range you provide. The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times

from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)