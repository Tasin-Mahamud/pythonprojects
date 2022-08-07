import random

userinput = input("Please Tell me all the names of the people "
                  "that you are hanging out with "
                  "{seperate the names with a comma}\n")

frndlist = userinput.split(",")

randomization = random.choice(frndlist)

print(randomization)

