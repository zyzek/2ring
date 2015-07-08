# encoding: utf-8
import machines as m
import tapes as t
import display as d
import time

# A Unary Adder in One Dimension
unacontext = m.MachineContext(t.Plane(['0000100000']))
unacontext.create_machine("machines/arithmetic/planunadd.tm")

# A Binary Adder in One Dimension
addcontext = m.MachineContext(t.Plane(['|10000111,101110101;']))
addcontext.create_machine("machines/arithmetic/planbinadd.tm")

# A Decimal Subtractor in Two Dimensions and with Many Working Parts
# This machine is more of a complex, working in concert.\nThe parent spawns workers whenever it needs them for subtasks.
sub = t.Plane(['  3241',
               '203196'])
subcontext = m.MachineContext(sub)
subcontext.create_machine("machines/arithmetic/subtract-composite/subtract.tm", (6,0))

# Conway's Life, Turingified.
field = t.Plane(
		["###########",
         ">      @@ #",
         "#     @@  #",
         "#  @@  @  #",
         "# @@      #",
         "#  @      <",
         "###########"])
concontext = m.MachineContext(field)
concontext.create_machine("machines/automata/conway/conway.tm", (1,1), 100000)

# A dumb tail-chaser.
course = t.Plane(
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
chacontext.create_machine("machines/snailchase.tm", (0,0))

# Langton's ant, in quadruplicate.
lancontext = m.MachineContext(t.Plane())
lancontext.create_machine("machines/automata/polylangton.tm", (0,0), 1000000)

mcontext = chacontext

d.init(mcontext)
d.running = False

while True:
	d.step()