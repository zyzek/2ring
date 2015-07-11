import machines as m
import display as d
import time

# A Unary Adder in One Dimension
unacontext = m.MachineContext(m.Plane(['0000100000']))
unacontext.create_machine("machines/arithmetic/unaryadder.tm")

# A Binary Adder in One Dimension
addcontext = m.MachineContext(m.Plane(['|10000111,101110101;']))
addcontext.create_machine("machines/arithmetic/compbinadd.tm")

# A Decimal Subtractor in Two Dimensions and with Many Working Parts
# This machine is more of a complex, working in concert.\nThe parent spawns workers whenever it needs them for subtasks.
sub = m.Plane(['  3241',
               '203196'])
subcontext = m.MachineContext(sub)
subcontext.create_machine("machines/arithmetic/subtract-composite/subtract.tm", (6,0))

# Conway's Life, Turingified.
field = m.Plane(
		["###########",
         ">      @@ #",
         "#     @@  #",
         "#      @  #",
         "#  @@     #",
         "# @@      #",
         "#  @      #",
         "#         #",
         "#         #",
         "#         <",
         "###########"])
concontext = m.MachineContext(field)
concontext.create_machine("machines/automata/conway/conway.tm", (1,1), None, 100000)

# A dumb tail-chaser.
course = m.Plane(
		  ["┌       {       ┐",
		  "                      ┌    ┐",
		  "                           ",
		  "'       >       u%    └         ┐",
		  "                           *",
		  "        *                  └    ┘",
		  "└       )       ^       {       ┐",
		  "",
		  "                *",
		  "                ,       v       i",
		  "",
		  "                                *",
		  "                └       (       ┘"])
chacontext = m.MachineContext(course)
chacontext.create_machine("machines/snailchase.tm")

# Langton's ant, in quadruplicate.
lancontext = m.MachineContext(m.Plane())
lancontext.create_machine("machines/automata/langton.tm", (0,0), "quad", 1000000)

# Random Walk
rancontext = m.MachineContext(m.Plane())
rancontext.create_machine("machines/randwalk.tm")

d.init(rancontext)
d.running = False

d.run()