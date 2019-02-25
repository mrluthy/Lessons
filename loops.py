# Lesson Objectives:
#     1. Implement If Statements with inputs.
#     2. Create For loops on their own.
#     3. Create While loops on their own.
#     4. Implement if, for, and while loops into a real world example.

# If statements selects certain actions to perform.

# Analogy:
#  Imagine going grocery shopping and your significant other asks you to get milk, pragmatically, you can look at
#       each aisle and if that aisle has milk, then you go down that aisle. Otherwise, go to the next aisle.

# Example:

# a = 200
# b = 30
#
# if b > a:
#     print('b is greater than a')
# elif a == b:
#     print('a and b are equal')
# else:
#     print("a is greater than b")

# Practice:
    # Print "Hello World" if A is greater than B

# a = 5
# b = 3
#
# if a > b:
#     print("Hello World")
# else:
#     print("Nope")


    # Create an if statement for feeding your pet. If your pet is hungry, print "FEED IT".
        # If not, print "LEAVE IT ALONE". *remember to define your variable.

# fluffy = "hungry"
#
# if fluffy == "hungry":
#     print("FEED IT")
# else:
#     print("LEAVE IT ALONE")

    # Create your own if statement that checks if an item in your grocery cart is down a particular aisle or not.
#       If it isn’t there, it needs to continue looking for that item. For example, say Milk is on aisle B, your
#       program should check aisle A, and then B and then exit your if statement.

# aisle_A = "cheese"
# aisle_B = "milk"
#
# if aisle_A == "milk":
#     print("Cheese is down this aisle")
# elif aisle_B == "milk":
#     print("Milk is down this aisle")
# else:
#     print("Where are you?")


# Now add user input and depending on the input, have the program go through the conditionals.

# A = input("Please type either milk or cheese: ")
# B = input("Please type either milk or cheese: ")
#
# if A.lower() == "milk":
#     print("Milk is down aisle A")
# elif B.lower() == "milk":
#     print("Milk is down aisle B")
# else:
#     print("This is not the aisle you are looking for?")

# Create an if statement to verify that the user input is at least 8 characters

# input = input("Please enter your Password: ")
#
# if len(input) < 8:
#     print("Your password is too short, please try again but with at least 6 characters: ")
# else:
#     print("Your password is long enough! ")

# One last example:

# monster_choice = input("Please input either Sully or Mike: ")
#
# if monster_choice.lower() == "sully":
#     print("Where are you Boo?")
# elif monster_choice.lower() == "mike":
#     print("Put that thing back where it came from or so help me!")
# else:
#     print("Run its a monster!")


# For Loops repeat a process for a limited number of times.
    # For for target in object: do something

# Analogy: During your grocery shopping, you need to check that you have gotten each of the items in your 10 item list.

#   Example:

# for x in "banana":
#     print(x)
#
# mylist = [1, 2, 3, 4, 5]
# list_sum = 0
#
# for num in mylist:
#     list_sum = list_sum + num
# print(list_sum)
#
# for num in mylist:
#     list_sum = list_sum + num
#     print(list_sum)

# for x in range(1, 100):
#     print(x)


# What is the difference in values when the print statement is indented?

# Practice: Using your 10 item grocery list and a for loop, print out each of the items in that list.

# grocery_list = ["Milk", "Cheese", "Bread", "Mustard", "Meat", "Chips", "Soda", "Candy", "Tomatoes", "Lettuce"]
#
# for target in grocery_list:
#     print(target)

# Compute all multiples of 3 and 8 that are less than 100

# new_range = 0
#
# for number in range(1, 100):
#     if number%3 == 0 or number%8 == 0:
#         new_range += number
# print(new_range)

# Break in a For Loop: Break stops the loop before it has looped through all of the items.

# Examples:

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#     if fruit == "banana":
#         break


# Practice: Break out of your loop once the 3rd item is printed out.

# grocery_list = ["Milk", "Cheese", "Bread", "Mustard", "Meat", "Chips", "Soda", "Candy", "Tomatoes", "Lettuce"]
#
# for target in grocery_list:
#     print(target)
#     if target == "Bread":
#         break


# For Continue: STOPS the current iteration and then continues onto the next iteration.

# Example:

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#     if fruit == "banana":
#         continue

# Practice: Using your grocery list, skip the 3rd item in the list.

# grocery_list = ["Milk", "Cheese", "Bread", "Mustard", "Meat", "Chips", "Soda", "Candy", "Tomatoes", "Lettuce"]
#
# for target in grocery_list:
#     print(target)
#     if target == "Bread":
#         continue

# Challenge: Print out a list of 10 grocery items using print, break, continue, for and if.

# grocery_list = ["Milk", "Cheese", "Bread", "Mustard", "Meat", "Chips", "Soda", "Candy", "Tomatoes", "Lettuce"]
#
# for target in grocery_list:
#     if target == "Bread":
#         continue
#     if target == "Candy":
#         break
#     print(target)

# Additional Practice:
#   Use for, .split() and if to create a statement that will print out the words that start with 's'.
#        str= "Print only the words that start with s in this sentence"

# str = 'Print only the words that start with s in this sentence'
# for word in str.split():
#     if word[0] == 's':
#         print(word)


#   Use range() to print all the even numbers from 0 - 10.

# for num in range(0,11,2):
#   print(num)


#   Go through the following string and print the words that have an even number of letters:
#       "Print every word in this sentence that has an even number of letters."

# str = 'Print every word in this sentence that has an even number of letters'
# # for word in str.split():
# #     if len(word)%2 == 0:
# #         print(word)


#   Write a program that prints a range of numbers from 1-100. For numbers divisible by 3 print "Fizz", numbers divisible
#         by 5 print "Buzz" and numbers divisible by both "FizzBuzz"

# for num in range(1, 101):
#     if num%3 == 0 and num%5 == 0:
#         print("Fizz Buzz")
#     elif num%5 == 0:
#         print("Buzz")
#     elif num%3 == 0:
#         print("Fizz")
#     else:
#         print(num)

# While Loops: Executes a set of statements as long as a condition (True or False) is true.

# Analogy: During your grocery shopping, keep shopping until all 10 items are in your cart.

# Example:

# x = 0
# while x < 10:
#     x += 1
#     print(x)

# Practice: Create your own while loop but make it only print if the value is less than 5.

# Can also incorporate breaks and continues into your while loop

# Examples:

# x = "spam"
# while x:
#     print(x, end=' ')
#     x = x[1:]

# x = 0
# while x < 10:
#     x += 1
#     if x == 3:
#         break
#     print(x)

# Practice:
#   Create a while loop for your grocery list to remove the first item during each iteration until the list is empty.

# grocery_list = ["Milk", "Cheese", "Bread", "Mustard", "Meat", "Chips", "Soda", "Candy", "Tomatoes", "Lettuce"]
#
# while grocery_list:
#     print(grocery_list)
#     grocery_list = grocery_list[1:]


# Challenge: Using your grocery list of 10 items, use a while loop, for loop, if statement.
#
# grocery_list = ["Milk", "Cheese", "Bread", "Mustard", "Meat", "Chips", "Soda", "Candy", "Tomatoes", "Lettuce"]
#
# while grocery_list:
#     for target in grocery_list:
#         if target == "Bread":
#             continue
#         if target == "Candy":
#             break
#         print(target)
#     grocery_list = grocery_list[1:]

