from entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

bandit = Entity(char="b", color=(255, 255, 255), name="Bandit", blocks_movement=True)
vampire = Entity(char="V", color=(255, 0, 0), name="Vampire", blocks_movement=True)
