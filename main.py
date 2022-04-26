"""My integration project"""
___author___ = "Kelly Allaire"

# Kelly Allaire
""" Here is my program to make the perfect Iced Coffee"""
# The general equation for iced coffee is
# IcedCoffee = Ice + Coffee + Cream + Flavor + Sugar

print("Hello, Good Morning!")

# Say hello to greet your user

print("How did you sleep last night?")
if input() == "good" or "Good" or "Great" or "great":
    print("Then you are starting today off on the right foot.")
else:
    print("Let's make a coffee to start your day off right!")

# You need to put the input after your question so that it is
# interactive and your user can respond.

print("What is on your agenda for today?")
print("1. Work "
      "2. School "
      "3. Self-care day "
      "4. Cleaning day "
      "5. Nothing ")

choice_1 = input()
if choice_1 == int():
    if choice_1 == 1:
        print("You are going to need more than just coffee")
    if choice_1 == 2:
        print("You are going to need it for all the studying.")
    if choice_1 == 3:
        print("What is a better way to start today then with a coffee.")
    if choice_1 == 4:
        print("You have a lot to do, so let's check off the first thing.")
    if choice_1 == 5:
        print("Seems like you have plenty of time to make this coffee. ")
else:
    print("Please enter a valid input!")

# Now it is time to get into making the perfect coffee

print("Have you had a cup of coffee yet?")
if str(input()) == "yes":
    print("Then you should quit this program now.")
else:
    print("Would you like me to help you make the perfect coffee?")

# print("Would you like me to help you make the perfect coffee?")
# input()

print("Do you prefer hot or iced coffee?")
if input() != "hot":
    print("Great choice")
elif input() == "iced" or "Iced":
    print("Great choice")
else:
    print("Try again. Only inputs allowed are 'hot' or 'iced'.")

# Keep asking questions so that they feel involved.
# It also is more of a conversation which people like
# instead of it just being a computer program.

# print("If you like iced coffee add 2 cups of ice into a 24oz tumbler")
# print("or if you are feeling fancy add 1 1/2 cups to a glass mason jar.")
# print("Now for the important part.")


print("Do you need to brew fresh coffee or do you have cold brew?")
if input() == "Brew" or "fresh" or "coffee":
    print("Pop a k-cup into your keurig.")
elif input() == "cold" and "brew":
    print("Then grab that cold brew from the fridge")
else:
    print("Now that you have coffee, let's move on")

# print("If you need to brew your coffee, pop a k-cup into your keurig.")
print("While we wait for that to brew, let's do some trivia.")

# Maybe later down the road, give them an option to skip this part
# but for right now it says.

# Personally I love trivia, and it is a great time killer while
# they need to brew their coffee. What trivia is better than
# math trivia?

print("What is 3 * 5?")
input()
print("The answer is ...", 3 * 5)

print("What is 4 ** 2?")
input()
print("The answer is ...", 4 ** 2)

print("What is 9 / 3")
input()
print("The answer is ....", 9 / 3)

print("What is 3612 // 2")
input()
print("The answer is ....", 3612 // 2)

print("What is 673 % 4")
input()
print("The answer is ....", 673 % 4)

print("What is 3 + 2 - 4?", end=' ')

input()
print("The answer is ... 1!")

numbers = [29, 93, 45, 61, 2, 15, 38, 56, 91, 72, 49]
for n in numbers:
    if n // 4 == 1:
        print("This works.")

m = input("Enter a number 1-10: ")
while m in numbers:
    if m * 2 == 30:
        print("This is a test")
    if m is range(1, 100):
        print("in range")
    else:
        print("Try again.")
else:
    print("please enter a valid input")


def getsmaller(num1, num2):
    """This function will compare two numbers and print the smaller one"""
    if num2 < num1:
        smaller = num2
    else:
        smaller = num1
    return smaller


def main():
    """This program will take two numbers and compare these numbers to see
    which number is smaller and then print that number with the string"""
    input1 = int(input("Enter a number 1-100: "))
    input2 = int(input("Enter another number 1-100: "))

    small = getsmaller(input1, input2)
    print("The smaller number is", small)

# if __name__ == " __main__ ":
#    main()

# If you don't return the functions they will not run

# This end will put the answer right at the end of the line and
# not on a new line.
# This isn't needed, but it is kind of different.


# This was mainly a way to get all the requirements in
# Now time to wrap it up

print("WAY TO GO!!!!", " Your coffee should be ready.", sep=" &")
print("Today is a good day to have a great day.")

# This was from geeks for geeks which was on the class website.
if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
