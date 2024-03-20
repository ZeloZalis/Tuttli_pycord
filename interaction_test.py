import random


with open(f"resources/attack.txt", "r") as file:
    response_list = file.readlines()
    response = random.choice(response_list)
print(response)