import random
with open("resources/battle/skills.txt") as file:
    attack_list = []
    read_lines = file.readlines()
    attack_list = random.sample(read_lines, 3)
    print(f"{attack_list}")