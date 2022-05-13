# Lessons learned today 10/15/2018:
# input() function
# while() function
# int() function
# % modulo function (remainder)
# += add 1 to the variable
# +=5 add 5 to the variable
# break exit the upper loop
# continue starts again at upper loop


message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

#7.2 activity
table = input("\nHow many people are in your dinner group?")
table = int(table)
if table > 8:
    print("\nYou will have to wait for a table")
else:
    print("\nPlease follow me to your table")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and  I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
if message != 'quit':
    print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#move ticket activity
active = True
while active:
    print("\nEnter 'quit' to end the program. ")
    age = input("\nHow old are you? ")
    if age == 'quit':
        active = False
    else:
        print("You are", age, "yeaers old")
        i_age = int(age)
    print(i_age)
    if i_age < 3:
        print("Your admission cost is $0.")
    elif i_age < 13:
        print("Your admission cost is $5.")