from abc import ABC


class Sell(ABC):
    def __init__(self, price_per_meter, discount, replacement, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discount = discount
        self.replacement = replacement
        super().__init__(*args, **kwargs)


class Rent(ABC):
    def __init__(self, mortgage, rent_money, changeable, discount, *args, **kwargs):
        self.mortgage = mortgage
        self.rent_money = rent_money
        self.changeable = changeable
        self.discount = discount
        super().__init__(*args, **kwargs)
