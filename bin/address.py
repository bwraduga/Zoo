
class ZooAddress:
    def __init__(self, home_id, section, desc):
        self.home_id = home_id
        self.section = section
        self.desc = desc

    def __str__(self):
        return f"Zoo Address - Section: {self.section}, {self.desc}"
