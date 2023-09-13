from environment import VacuumEnvironment
from agent import SimpleVacuumAgent

if __name__ == "__main__":
    width = 2
    height = 2
    dirt_locations = [(0,0),(1,1)]

    environment = VacuumEnvironment(width, height, dirt_locations)
    environment.place_agent((0, 0))

    agent = SimpleVacuumAgent(environment)
    actions = agent.plan_actions()
    environment.run(actions)
