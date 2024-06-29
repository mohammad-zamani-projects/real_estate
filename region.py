
class Region:
    def __init__(self, region_name, *args, **kwargs):
        self.region_name = region_name
        super().__init__(*args, **kwargs)

    @property
    def show_address(self):
        return self.region_name
