from random import randint


class Product(object):
    """Base ACME product.

    :param name: str
    :param price: int default = 10
    :param weight: int default = 20
    :param flammability: float default = 0.5

    """

    def __init__(self,
                 name: str,
                 price: int = 10,
                 weight: int = 20.0,
                 flammability: float = 0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """Calculate stealability of product.

        stealability = price / weight

        :return: str
        """
        steal = self.price / self.weight
        if steal < 0.5:
            return 'Not so stealable...'
        if 0.5 <= steal < 1:
            return 'Kinda stealable.'
        return 'Very stealable!'

    def explode(self):
        """Calculate explodability of product.

        eplodability = flammability * weight

        :return: str
        """
        stable = self.flammability * self.weight
        if stable < 10:
            return '...fizzle.'
        if 10 <= stable < 50:
            return '...boom!'
        return '...BABOOM'


class BoxingGlove(Product):
    """ACME Boxing glove.

    Inherits from Product.
    Overrides explode.

    """

    def __init__(self, name):
        super(BoxingGlove, self).__init__(name=name)
        self.weight = 10

    def explode(self):
        """This product cannot explode.

        :return: str
        """
        return '...it\'s a glove'

    def punch(self):
        """Calculate punch strength of glove.

        :return:
        """
        if self.weight > 5:
            return 'That tickles'
        if 5 <= self.weight < 15:
            return 'Hey that hurt!'
        return 'OUCH!'


if __name__ == "__main__":
    pass
