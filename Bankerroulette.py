# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
a=len(names)
#Write your code below this line 👇

randomnumber=random.randrange(0,a-1)
print(f"{names[randomnumber]} is going to buy the meal today!")