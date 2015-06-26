# encoding: utf-8
import machines as m
import tapes as t
import time


print("A Unary Adder in One Dimension")
time.sleep(1)
u = m.parse_machine("machines/unaryadder.tm")
u.run(t.Tape("0000100000"), 0, display=True, delay=0.1)
time.sleep(1)

print("\nA Binary Adder in One Dimension")
time.sleep(1)
b_tape1 = t.Tape('|10000111,101110101;')
b_tape2 = t.Tape('|1101,11001;')
b_add = m.parse_machine("machines/compactedbinaryadder.tm")
b_add.run(b_tape1, 0, display=True, delay=0.01)
time.sleep(1)

print("\nA Decimal Subtractor in Two Dimensions and with Many Working Parts")
print("This machine is more of a complex, working in concert.\nThe parent spawns workers whenever it needs them for subtasks.")
time.sleep(5)

sub = t.Plane(['  3241',
               '203196'])
d_sub = m.parse_machine("machines/subtract-composite/subtract.tm")
d_sub.run(sub, pos=(6,0), display=True, delay=0.1)

print("\nConway's Life, Turingified.")
time.sleep(1)
field = ["###########",
         ">      @@ #",
         "#     @@  #",
         "#  @@  @  #",
         "# @@      #",
         "#  @      <",
         "###########"]
con = m.parse_machine("machines/conway/conway.tm", 10000)
con.run(t.Plane(field), (1,1), display=True, delay=0)

print("\nA dumb tail-chaser.")
time.sleep(1)
course = ["┌       {       ┐",
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
		  "                └       (       ┘"]
chaser = m.parse_machine("machines/snailchase.tm")
chaser.run(t.Plane(course), (0,0), display=True, delay=0.03)