class SimpleVacuumAgent:
    def __init__(self, environment):
        self.environment = environment

    def plan_actions(self):
        actions = []
        for location in self.environment.dirt_locations:
            x, y = location
            if x < self.environment.agent_location[0]:
                actions.append('left')
            elif x > self.environment.agent_location[0]:
                actions.append('right')
            if y < self.environment.agent_location[1]:
                actions.append('down')
            elif y > self.environment.agent_location[1]:
                actions.append('up')
            actions.append('suck')
        return actions
