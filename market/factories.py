from faker import Faker
from faker.providers import bank


class ProductFactory(object):
    def __init__(self):
        fake = Faker()
        fake.add_provider(bank)
        self.id = fake.bban()
        self.buy_price = fake.pydecimal(left_digits=3, right_digits=4, positive=True)
        self.sell_price = fake.pydecimal(left_digits=3, right_digits=4, positive=True)
        self.description = fake.text()

    def __repr__(self):
        return f"""<ProductFactory
            {self.id=}
            {self.buy_price=}
            {self.sell_price=}
            {self.description=}
            >"""
