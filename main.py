print("This is an awesome quiz game. Hope you enjoy it")

playing = input("Are you ready to play? ")

if playing != "yes":
    quit()

print("Let's begin :)")
score = 0


puzzle1 = input("Pus-filled swelling: scab's broken round edges of ears. ")
if puzzle1 == "Abscess":
    print("That is correct!")
    score += 1
else:
    print("That is not the correct answer!")

puzzle1 = input("Cucumber is a bit tougher, kinked. ")
if puzzle1 == "Gherkin":
    print("Wonderful brain!")
    score += 1
else:
    print("Are you sure?")

puzzle1 = input("Sam dreamt about a European Port. ")
if puzzle1 == "Amsterdam":
    print("You are awesome!")
    score += 1
else:
    print("Better luck next time!")

puzzle1 = input("Inexperienced band intended to limit urban sprawl. ")
if puzzle1 == "Greenbelt":
    print("Good job!")
    score += 1
else:
    print("Too bad!")

print("You got " + str(score) + " questions correct!")
print("Your total percentage is " + str((score / 4) * 100) + "%.")
