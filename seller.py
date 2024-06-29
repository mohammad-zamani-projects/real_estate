

class Seller:
    def __init__(self, name, number, *args, **kwargs):
        self.name = name
        self.number = number
        super().__init__(*args, **kwargs)
