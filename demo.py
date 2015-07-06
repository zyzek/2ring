# encoding: utf-8
import machines as m
import tapes as t
import display as d
import time

sub = t.Plane(['  3241',
               	   '203196'])
subcontext = m.MachineContext(sub)
subcontext.create_machine("machines/subtract-composite/subtract.tm", (6,0))

field = t.Plane(
		["###########",
         ">      @@ #",
         "#     @@  #",
         "#  @@  @  #",
         "# @@      #",
         "#  @      <",
         "###########"])
concontext = m.MachineContext(field)
concontext.create_machine("machines/conway/conway.tm", (1,1), 100000)

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

lancontext = m.MachineContext(t.Plane())
lancontext.create_machine("machines/polylangton.tm", (0,0), 1000000)


addcontext = m.MachineContext(t.Plane(['|10000111,101110101;']))
addcontext.create_machine("machines/planbinadd.tm")

mcontext = chacontext

d.init()

while True:
	d.step(mcontext)

"""
print("A Unary Adder in One Dimension")
time.sleep(1)
u = m.parse_machine("machines/unaryadder.tm")
u.run(t.Tape("0000100000"), 0, display=True, delay=0.1)
time.sleep(1)

print("\nA Binary Adder in One Dimension")
print("\nA Decimal Subtractor in Two Dimensions and with Many Working Parts")
print("This machine is more of a complex, working in concert.\nThe parent spawns workers whenever it needs them for subtasks.")
print("\nConway's Life, Turingified.")
print("\nA dumb tail-chaser.")
"""