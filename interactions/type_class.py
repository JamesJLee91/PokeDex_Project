class Type:
    def __init__(self, name):
        self.name = name
        self.effectiveness = {}

    def add_effectiveness(self, other_type, multiplier):
        self.effectiveness[other_type] = multiplier

    def get_effectiveness(self, other_type):
        return self.effectiveness.get(other_type, 1.0)

    def __repr__(self):
        return self.name
