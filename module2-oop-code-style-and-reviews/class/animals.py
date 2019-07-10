from fauna import *

paul = Human('Paul', 40)
banjo = Doggo('Banjo', 7)
chichi = Iguana('Chichi', 3)

paul.speak()
banjo.speak()
chichi.speak()

paul.move_down()
paul.move_down()

banjo.move_up()
banjo.move_up()

print(f'Chichi has hair? {chichi.hair == True}')
