import random

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf',
         'Half-Orc', 'Halfling', 'Human', 'Tiefling']

friends = ['Jon', 'Shannon', 'Max', 'Tommy', 'Tara', 'Maggie', 'Richard',
           'T.Robert', 'Nathan', 'Andrew', 'Peter', 'Art', 'Sam', 'Bryce']

characters = {}

for friend in friends:
    characters.setdefault(friend, [])
    char_class = classes[random.randint(0, len(classes)-1)]
    if random.randint(1, 42) == 42:
        char_class += "-" + classes[random.randint(0, len(classes)-1)]
    char_race = races[random.randint(0, len(races)-1)]
    characters[friend].append(char_race)
    characters[friend].append(char_class)
    characters[friend].append(str(random.randint(1, 20)))

output = ["name, race, class, level"]
for key, value in characters.items():
    output.append(key + "," + value[0] + "," + value[1] + "," + value[2])

print(len(output))

with open('classes.csv', 'w') as f:
    for item in output:
        f.write(item + "\n")
