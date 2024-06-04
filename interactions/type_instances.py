from .type_class import Type

# Creating type instances
normal = Type("Normal")
fire = Type("Fire")
water = Type("Water")
electric = Type("Electric")
grass = Type("Grass")
ice = Type("Ice")
fighting = Type("Fighting")
poison = Type("Poison")
ground = Type("Ground")
flying = Type("Flying")
psychic = Type("Psychic")
bug = Type("Bug")
rock = Type("Rock")
ghost = Type("Ghost")
dragon = Type("Dragon")
dark = Type("Dark")
steel = Type("Steel")
fairy = Type("Fairy")

# Define effectiveness
# Normal
normal.add_effectiveness(rock, 0.5)
normal.add_effectiveness(ghost, 0.0)
normal.add_effectiveness(steel, 0.5)

# Fire
fire.add_effectiveness(fire, 0.5)
fire.add_effectiveness(water, 0.5)
fire.add_effectiveness(grass, 2.0)
fire.add_effectiveness(ice, 2.0)
fire.add_effectiveness(bug, 2.0)
fire.add_effectiveness(rock, 0.5)
fire.add_effectiveness(dragon, 0.5)
fire.add_effectiveness(steel, 2.0)

# Water
water.add_effectiveness(fire, 2.0)
water.add_effectiveness(water, 0.5)
water.add_effectiveness(grass, 0.5)
water.add_effectiveness(ground, 2.0)
water.add_effectiveness(rock, 2.0)
water.add_effectiveness(dragon, 0.5)

# Electric
electric.add_effectiveness(water, 2.0)
electric.add_effectiveness(electric, 0.5)
electric.add_effectiveness(ground, 0.0)
electric.add_effectiveness(flying, 2.0)
electric.add_effectiveness(dragon, 0.5)

# Grass
grass.add_effectiveness(fire, 0.5)
grass.add_effectiveness(water, 2.0)
grass.add_effectiveness(grass, 0.5)
grass.add_effectiveness(poison, 0.5)
grass.add_effectiveness(ground, 2.0)
grass.add_effectiveness(flying, 0.5)
grass.add_effectiveness(bug, 0.5)
grass.add_effectiveness(rock, 2.0)
grass.add_effectiveness(dragon, 0.5)
grass.add_effectiveness(steel, 0.5)

# Ice
ice.add_effectiveness(fire, 0.5)
ice.add_effectiveness(water, 0.5)
ice.add_effectiveness(grass, 2.0)
ice.add_effectiveness(ice, 0.5)
ice.add_effectiveness(ground, 2.0)
ice.add_effectiveness(flying, 2.0)
ice.add_effectiveness(dragon, 2.0)
ice.add_effectiveness(steel, 0.5)

# Fighting
fighting.add_effectiveness(normal, 2.0)
fighting.add_effectiveness(ice, 2.0)
fighting.add_effectiveness(poison, 0.5)
fighting.add_effectiveness(flying, 0.5)
fighting.add_effectiveness(psychic, 0.5)
fighting.add_effectiveness(bug, 0.5)
fighting.add_effectiveness(rock, 2.0)
fighting.add_effectiveness(ghost, 0.0)
fighting.add_effectiveness(dark, 2.0)
fighting.add_effectiveness(steel, 2.0)
fighting.add_effectiveness(fairy, 0.5)

#Poison
poison.add_effectiveness(grass, 2.0)
poison.add_effectiveness(poison, 0.5)
poison.add_effectiveness(ground, 0.5)
poison.add_effectiveness(rock, 0.5)
poison.add_effectiveness(ghost, 0.5)
poison.add_effectiveness(steel, 0.0)
poison.add_effectiveness(fairy, 2.0)

#Ground
ground.add_effectiveness(fire, 2.0)
ground.add_effectiveness(electric, 2.0)
ground.add_effectiveness(grass, 0.5)
ground.add_effectiveness(poison, 2.0)
ground.add_effectiveness(flying, 0.0)
ground.add_effectiveness(bug, 0.5)
ground.add_effectiveness(rock, 2.0)
ground.add_effectiveness(steel, 2.0)

#Flying
flying.add_effectiveness(electric, 0.5)
flying.add_effectiveness(grass, 2.0)
flying.add_effectiveness(fighting, 2.0)
flying.add_effectiveness(bug, 2.0)
flying.add_effectiveness(rock, 0.5)
flying.add_effectiveness(steel, 0.5)

#Psychic
psychic.add_effectiveness(fighting, 2.0)
psychic.add_effectiveness(poison, 2.0)
psychic.add_effectiveness(psychic, 0.5)
psychic.add_effectiveness(dark, 0.0)
psychic.add_effectiveness(steel, 0.5)

#Bug
bug.add_effectiveness(fire, 0.5)
bug.add_effectiveness(grass, 2.0)
bug.add_effectiveness(fighting, 0.5)
bug.add_effectiveness(poison, 0.5)
bug.add_effectiveness(flying, 0.5)
bug.add_effectiveness(psychic, 2.0)
bug.add_effectiveness(ghost, 0.5)
bug.add_effectiveness(dark, 2.0)
bug.add_effectiveness(steel, 0.5)
bug.add_effectiveness(fairy, 0.5)

# Rock
rock.add_effectiveness(fire, 2.0)
rock.add_effectiveness(ice, 2.0)
rock.add_effectiveness(fighting, 0.5)
rock.add_effectiveness(ground, 0.5)
rock.add_effectiveness(flying, 2.0)
rock.add_effectiveness(bug, 2.0)
rock.add_effectiveness(steel, 0.5)

# Ghost
ghost.add_effectiveness(normal, 0.0)
ghost.add_effectiveness(psychic, 2.0)
ghost.add_effectiveness(ghost, 2.0)
ghost.add_effectiveness(dark, 0.5)

# Dragon
dragon.add_effectiveness(dragon, 2.0)
dragon.add_effectiveness(steel, 0.5)
dragon.add_effectiveness(fairy, 0.0)

# Dark
dark.add_effectiveness(fighting, 0.5)
dark.add_effectiveness(psychic, 2.0)
dark.add_effectiveness(ghost, 2.0)
dark.add_effectiveness(dark, 0.5)
dark.add_effectiveness(fairy, 0.5)

# Steel
steel.add_effectiveness(fire, 0.5)
steel.add_effectiveness(water, 0.5)
steel.add_effectiveness(electric, 0.5)
steel.add_effectiveness(ice, 2.0)
steel.add_effectiveness(rock, 2.0)
steel.add_effectiveness(steel, 0.5)
steel.add_effectiveness(fairy, 2.0)

# Fairy
fairy.add_effectiveness(fire, 0.5)
fairy.add_effectiveness(fighting, 2.0)
fairy.add_effectiveness(poison, 0.5)
fairy.add_effectiveness(dragon, 2.0)
fairy.add_effectiveness(dark, 2.0)
fairy.add_effectiveness(steel, 0.5)

all_types = [normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost,
             dragon, dark, steel, fairy]

type_dict = {type_instances.name.lower(): type_instances for type_instances in all_types}
