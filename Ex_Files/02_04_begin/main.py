NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 1
#while is prone to endless looping
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)
#zip pulls together the lists
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i + 1)

# enumerate

for i, name in enumerate(NAMES):
    print(f'{i} {name}')