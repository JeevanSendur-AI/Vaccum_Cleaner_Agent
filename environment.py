class VacuumEnvironment:
    def __init__(self, width, height, dirt_locations):
        self.width = width
        self.height = height
        self.dirt_locations = dirt_locations
        self.agent_location = (0, 0)
        self.performance_measure = 0

    def place_agent(self, location):
        self.agent_location = location

    def is_dirty(self, location):
        return location in self.dirt_locations

    def clean(self):
        if self.is_dirty(self.agent_location):
            self.dirt_locations.remove(self.agent_location)
            self.performance_measure += 1

    def move(self, action):
        x, y = self.agent_location
        if action == 'left' and x > 0:
            self.agent_location = (x - 1, y)
            self.performance_measure -= 1
        elif action == 'right' and x < self.width - 1:
            self.agent_location = (x + 1, y)
            self.performance_measure -= 1
        elif action == 'up' and y < self.height - 1:
            self.agent_location = (x, y + 1)
            self.performance_measure -= 1
        elif action == 'down' and y > 0:
            self.agent_location = (x, y - 1)
            self.performance_measure -= 1

    def run(self, actions):
        for action in actions:
            if action == 'suck':
                self.clean()
            else:
                self.move(action)
            print(f"Action: {action}, Location: {self.agent_location}, Performance: {self.performance_measure}")