from estate import House, Apartment, Store
from deal import Sell, Rent


class HouseSell(House, Sell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HouseRent(House, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ApartmentSell(Apartment, Sell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ApartmentRent(Apartment, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StoreSell(Store, Sell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StoreRent(Store, Rent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
