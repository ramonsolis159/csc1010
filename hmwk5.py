# Ramon Montoya
# This program is for an assignment.

# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

names = ['Brian', 'Bryan', 'Sabino', 'Vianey', 'Abby', 'Eli', 'Diana', 'Alex']
print(names)

print()

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.

names = ['Brian', 'Bryan', 'Sabino', 'Vianey', 'Abby', 'Eli', 'Diana', 'Alex']
greeting = "Hello there, "

print(greeting + names[0] + ".")
print(greeting + names[1] + ".")
print(greeting + names[2] + ".")
print(greeting + names[3] + ".")
print(greeting + names[4] + ".")
print(greeting + names[5] + ".")
print(greeting + names[6] + ".")
print(greeting + names[7] + ".\n")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

cars = ['1988 Ford Mustang GT', '1998 Toyota Supra', '1999 Nissan Skyline GTR R34']
statement = "I would like to own a "

print(statement + cars[0] + ".")
print(statement + cars[1] + ".")
print(statement + cars[2] + ".\n")

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guests = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar Junior', 'Javier Hernandez']
invitation = "Hello, I would like to invite you to a dinner, "

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".\n\n")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.

guests = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar Junior', 'Javier Hernandez']
invitation = "Hello, I would like to invite you to a dinner, "

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".\n")

print(guests[2] + " unfortunately will not be able to make it to the dinner.\n")

guests[2] = 'Pele'

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".\n\n")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

guests = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar Junior', 'Javier Hernandez']
invitation = "Hello, I would like to invite you to a dinner, "

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".\n")

print(guests[2] + " unfortunately will not be able to make it to the dinner.\n")

guests[2] = 'Pele'

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".\n")

print("Hello everyone, I have found a bigger dinner table for the dinner that we will be having. Thanks!\n")

guests.insert(0, 'Guillermo Ochoa')
guests.insert(2, 'Paul Pogba')
guests.append('Wayne Rooneey')

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".")
print(invitation + guests[4] + ".")
print(invitation + guests[5] + ".")
print(invitation + guests[6] + ".\n\n")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.

guests = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar Junior', 'Javier Hernandez']
invitation = "Hello, I would like to invite you to a dinner, "

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".\n")

print(guests[2] + " unfortunately will not be able to make it to the dinner.\n")

guests[2] = 'Pele'

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".\n")

print("Hello everyone, I have found a bigger dinner table for the dinner that we will be having. Thanks!\n")

guests.insert(0, 'Guillermo Ochoa')
guests.insert(2, 'Paul Pogba')
guests.append('Wayne Rooneey')

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".")
print(invitation + guests[4] + ".")
print(invitation + guests[5] + ".")
print(invitation + guests[6] + ".\n")

print("Hello everyone, unfortunately I can only invite two people for dinner. I hope that you understand, thanks.\n")

sorry = "Sorry unfortunately I can not invite you to dinner. Maybe next time, "

popped_guests = guests.pop()
print(sorry + popped_guests + ".")
popped_guests = guests.pop()
print(sorry + popped_guests + ".")
popped_guests = guests.pop()
print(sorry + popped_guests + ".")
popped_guests = guests.pop()
print(sorry + popped_guests + ".")
popped_guests = guests.pop()
print(sorry + popped_guests + ".\n")

still_invited = "Hello there, I am glad to let you know that you are still " \
                "invited to the dinner. Thanks and see you soon, "

print(still_invited + guests[0] + ".")
print(still_invited + guests[1] + ".\n")

del guests[0]
del guests[0]
print(guests)

print()

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.

visit = ['Italy', 'New York', 'London', 'Sydney', 'Rome']

print("Here is the original list:")
print(visit)

print("\nHere is the sorted list:")
print(sorted(visit))

print("\nHere is the original list again:")
print(visit)

print("\nHere is the sorted list in reverse:")
print(sorted(visit,reverse=True))

print("\nHere is the original list again:")
print(visit)

print("\nHere is the list in reverse order:")
visit.reverse()
print(visit)

print("\nHere is the reversed order list back in the original list form")
visit.reverse()
print(visit)

print("\nHere is the stored list in alphabetical order")
visit.sort()
print(visit)

print("\nHere is the stored list in reverse alphabetical order")
visit.sort(reverse=True)
print(visit)

print()

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

guests = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar Junior', 'Javier Hernandez']
invitation = "Hello, I would like to invite you to a dinner, "

print(invitation + guests[0] + ".")
print(invitation + guests[1] + ".")
print(invitation + guests[2] + ".")
print(invitation + guests[3] + ".\n")

print(len(guests))

print()

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['pepperoni', 'sausage', 'bacon', 'chicken', 'ham', 'pineapple']
for pizza in pizzas:
    print(pizza)

print()

# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.

animals = ['lions', 'tigers', 'cheetahs', 'pumas', 'panthers']
for animal in animals:
    print(animal)

print()

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

for value in range(1, 21):
    print(value)

print()

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.

numbers = list(range(1, 1000001))
print(numbers)

print()

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

numbers = list(range(1, 1000001))
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print()

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

print()

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

multiples_threes = list(range(3, 31, 3))
print(multiples_threes)

print()

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubes = []
for value in range(1, 11):
    cubes.append(value**3)

print(cubes)

print()

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.

cubes = [value**3 for value in range(1, 11)]
print(cubes)

print()

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

pizza = ['pepperoni', 'sausage', 'bacon', 'chicken', 'ham', 'pineapple']

print("The first three items in the list are:")
print(pizza[0:3])

print("\nThe first three items from the middle of the list are:")
print(pizza[1:4])

print("\nThe last three items in the list are:")
print(pizza[3:])

print()

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:

pizzas = ['pepperoni', 'sausage', 'bacon', 'chicken', 'ham', 'pineapple']
friend_pizzas = pizzas[:]

pizzas.append('mushrooms')
friend_pizzas.append('black olives')

print("My favorite pizzas are:")
print(pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

print()

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print()

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.

foods = ('Salmon', 'Potatoes', 'Chicken', 'Sardines', 'Shrimp', 'Pork Chops')
print("Original food menu:")
for food in foods:
    print(food)

foods = ('Salmon', 'Potatoes', 'Chicken', 'Pasta', 'Meatballs', 'Pork Chops')
print("\nModified food menu:")
for food in foods:
    print(food)

print()

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

string = 'SUBARU'
print("\nIs car == 'lowercase'? I predict True")
print(string.lower())

string = 'Subaru'
print("\nIs car == 'lowercase'? I predict False")
print(string.lower())

string = 'subaru'
print("\nIs car == 'uppercase'? I predict True")
print(string.upper())

string = 'subaru'
print("\nIs car == 'uppercase'? I predict False")
print(string.upper())

print()

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")

print()

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

print()

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

print()

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:

age = 12

if age < 2:
    print("You are a baby.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder.")

print()

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list

favorite_fruits = ['apples', 'oranges', 'grapes']

if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'oranges' in favorite_fruits:
    print("You really like oranges!")
if 'grapes' in favorite_fruits:
    print("You really like grapes!")
if 'pears' in favorite_fruits:
    print("You really like pears")
if 'bananas' in favorite_fruits:
    print("You really like bananas")

print()

# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:

usernames = ['admin', 'rmontoya', 'Chololatino', 'Dragkiller159', 'ramen_noodlez', 'elmonchis123']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")

print()

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")

print()

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.

current_users = ['admin', 'rmontoya', 'Chololatino', 'Dragkiller159', 'ramen_noodlez', 'elmonchis123']

new_users = ['Chololatino', 'Dragkiller159', 'ElChavo', 'Maruchan', 'SpiderMan', 'David']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry that username is already taken. Please enter a new username.")
    else:
        print("That username is available.")

print()

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

