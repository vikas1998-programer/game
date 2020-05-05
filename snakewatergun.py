import random
list = ['s','w','g']

Chance = 4
Number_of_Chance = 0
Computer_Point = 0
Human_Point = 0

print(" s for Snake \n s for Water\n g for Gun\n")

# choice = input("Enter your choice")
while(Number_of_Chance < Chance):
    _input = input("s for Snake,w for Water,g for Gun :")
    _random = random.choice(list)

    if input ==_random :
        print("Tie Both 0 Point to  each \n")
         #input s
    if _input == "s" and _random == "g":
        Computer_Point = Computer_Point + 1
        print(f"your guess {input} and computer guess is {_random} \n")
        print(f"Computer_Point is {Computer_Point} and your point is {Human_Point} \n")

    elif _input == "s" and _random == "w":
        Human_Point = Human_Point + 1
        print(f"your guess {input} and computer guess is {random}")
        print(f"Computer_point is {Computer_Point} and your point is {Human_Point}")
        #input w
    elif _input == "w" and _random == "g":
        Human_Point = Human_Point +1
        print(f"your guess {input} and computer guess is {_random}")
        print(f"Computer_Point is {Computer_Point} and your point is {Human_Point}")

    elif _input == "w" and random == "s":
        Computer_Point = Computer_Point + 1
        print(f"your guess {input} and computer guess {_random}" )
        print(f"Computer_point is {Computer_Point} and your point is {Human_Point}")

        #input g

    elif _input == "g" and _random == "s":
        Human_Point = Human_Point + 1
        print(f"your guess {_input} and computer guess {_random}")
        print(f"Computer_point is {Computer_Point} and your point is {Human_Point}")

    elif _input == "g" and _random == "w":
        Computer_Point = Computer_Point + 1
        print(f"your guess {_input} and computer guess {_random}")
        print(f"Computer_point is {Computer_Point} and your point is {Human_Point}")

    else:
        print(f"you have input wrong \n")

    Number_of_Chance = Number_of_Chance + 1
    print(f"{Chance - Number_of_Chance} is left out of {Chance} \n")
print("Game Over")

if Computer_Point > Human_Point:
    print("Computer Wins and You loss")

elif Computer_Point < Human_Point :
    print("Human is Win and Computer Loss")

print(f"Your Point is {Human_Point} and Computer POint is {Computer_Point} \n")

