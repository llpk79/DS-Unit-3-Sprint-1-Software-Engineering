from fauna import *

paul = Human('Paul', 40)
banjo = Doggo('Banjo', 7)
chichi = Iguana('Chichi', 3)

paul.speak()
banjo.speak()
chichi.hiss()

paul.move_down()
paul.move_down()

banjo.move_up()
banjo.move_up()

print(f'Chichi has hair? {chichi.hair == True}')
print(f'Chichi has scales? {chichi.scales}')
print(f'{paul.name} is a {paul.age} year old {paul.species}')