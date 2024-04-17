import random
with open("resources/battle/skills.txt", encoding="utf-8") as file:
    attack_list = []
    read_lines = file.readlines()
    attack_list = random.sample(read_lines, 3)

#Transformo la lista de cadenas en una lista con diccionarios
diccio = [eval(i) for i in attack_list]
print(diccio)
