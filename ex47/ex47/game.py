class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.weapon = []

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_weapon(self, weapon):
        self.weapon.extend(weapon)

    def acquire_weapon(self, acquired):
        return self.weapon[acquired]

    
        
