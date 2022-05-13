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