from base import BaseClass


class Estate(BaseClass):
    def __init__(self, seller, area, room_count, building_age, region, address, usage, *args, **kwargs):
        self.seller = seller
        self.area = area
        self.room_count = room_count
        self.building_age = building_age
        self.region = region
        self.address = address
        self.usage = usage  # usage must be one of the "commercial", "official" or "residential"
        super().__init__(*args, **kwargs)


class House(Estate):
    def __init__(self, yard, number_of_floors, *args, **kwargs):
        self.yard = yard
        self.number_of_floors = number_of_floors
        super().__init__(*args, **kwargs)


class Apartment(Estate):
    def __init__(self, elevator, parking, floors, *args, **kwargs):
        self.elevator = elevator
        self.parking = parking
        self.floors = floors
        super().__init__(*args, **kwargs)


class Store(Estate):
    def __init__(self, shop_usage, *args, **kwargs):
        self.shop_usage = shop_usage
        super().__init__(*args, **kwargs)
