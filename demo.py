import machines as m
import display as d
import time

"""
# A Unary Adder in One Dimension
unacontext = m.MachineContext(m.Plane(['0000100000']))
unacontext.create_machine("machines/arithmetic/adders/unaryadder.tm")

# A Binary Adder in One Dimension
addcontext = m.MachineContext(m.Plane(['|10000111,101110101;']))
addcontext.create_machine("machines/arithmetic/adders/compbinadd.tm")

# A Decimal Subtractor in Two Dimensions and with Many Working Parts
# This machine is more of a complex, working in concert.\nThe parent spawns workers whenever it needs them for subtasks.
subcontext = m.MachineContext(m.parse_tape("machines/arithmetic/subtract-composite/subtract.tp"))
subcontext.create_machine("machines/arithmetic/subtract-composite/subtract.tm")

# Conway's Life, Turingified.
concontext = m.MachineContext(m.parse_tape("machines/automata/conway/conway.tp"))
concontext.create_machine("machines/automata/conway/conway.tm", lifespan=100000)

# A dumb tail-chaser.
chacontext = m.MachineContext(m.parse_tape("machines/misc/snailchase.tp"))
chacontext.create_machine("machines/misc/snailchase.tm")

# Langton's ant, in quadruplicate.
lancontext = m.MachineContext(m.Plane())
lancontext.create_machine("machines/automata/langton.tm", (0,0), "quad", 1000000)
"""
# Random Walk
rancontext = m.MachineContext(m.Plane())
rancontext.create_machine("machines/misc/randwalk.tm")


d.init(rancontext)
d.running = False
d.run()