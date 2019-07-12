import unittest
from fauna import Animal, Doggo, Iguana


class TestAnimals(unittest.TestCase):

    def test_init(self):
        anim = Animal('Anim', 40)
        self.assertTrue(isinstance(anim, Animal))
        self.assertEqual(anim.name, 'Anim')
        self.assertEqual(anim.age, 40)

    def test_move_up(self):
        anim = Animal('Anim', 40)
        self.assertEqual(anim.position, 0)
        anim.move_up()
        self.assertEqual(anim.position, 1)

    def test_move_down(self):
        anim = Animal('Anim', 40)
        self.assertEqual(anim.position, 0)
        anim.move_down()
        self.assertEqual(anim.position, -1)

    def test_speak(self):
        dog = Doggo('Watson', 11)
        self.assertEqual(dog.speak(), f'{dog.name} says "Woof"')

    def test_hiss(self):
        lizi = Iguana('Lizi', 3)
        self.assertEqual(lizi.hiss(), f'{lizi.name} says "Hiss"')

    def test_hair(self):
        lizi = Iguana('Lizi', 3)
        dog = Doggo('Watson', 11)
        self.assertTrue(dog.hair)
        self.assertFalse(lizi.hair)

    def test_scales(self):
        lizi = Iguana('Lizi', 3)
        dog = Doggo('Watson', 11)
        self.assertTrue(lizi.scales)
        self.assertFalse(dog.scales)


if __name__ == "__main__":
    unittest.main()
