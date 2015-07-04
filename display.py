import machines, tapes
import pygame, sys, os, time
from pygame.locals import *
pygame.init()

delay = 0.1
symsize = 16
symbols = {}
size = (800, 600)
origin = (size[0]/4, size[1]/4)
screen = None 

string = []
cursor = [0,0]

symdict = {}
symdict["*"] = "star"
symdict["<"] = "langbrack"
symdict[">"] = "rangbrack"

def init():
	global screen
	global symbols

	screen = pygame.display.set_mode(size, pygame.RESIZABLE)
	for filename in os.listdir("symbols/"):
		key = filename[:-4]
		if key.endswith("_"):
			key = key[:-1]

		symbols[key] = pygame.transform.smoothscale(pygame.image.load("symbols/" + filename), (symsize,symsize))

def get_sym_img(symbol):

	try:
		return symbols[symbol]
	except KeyError:
		try:
			return symbols[symdict[symbol]]
		except KeyError:
			return symbols["ERR"]

def display_tape(mcontext):
	for point in mcontext.tape:
		coords = (origin[0] + point[0]*symsize, origin[1] + point[1]*symsize)
		screen.blit(get_sym_img(mcontext.tape[point]), coords)

init()
sub = tapes.Plane(['  3241',
               	   '203196'])
subcontext = machines.MachineContext(sub)
subcontext.create_machine("machines/subtract-composite/subtract.tm", (6,0))

field = tapes.Plane(
		["###########",
         ">      @@ #",
         "#     @@  #",
         "#  @@  @  #",
         "# @@      #",
         "#  @      <",
         "###########"])
concontext = machines.MachineContext(field)
concontext.create_machine("machines/conway/conway.tm", (1,1), 100000)

course = tapes.Plane(
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
chacontext = machines.MachineContext(course)
chacontext.create_machine("machines/snailchase.tm", (0,0))

mcontext = chacontext

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.unicode.isalnum():
				string.append(event.unicode)
			elif event.key == K_SPACE:
				string.append("space")
			elif event.key == K_ESCAPE:
				sys.exit()
			elif event.key == K_BACKSPACE and len(string) != 0:
				string.pop()

	screen.fill((0,0,0))
	
	cursor = [0,0]
	for letter in string:
		screen.blit(symbols[letter], cursor)
		cursor[0] += symsize

		if cursor[0] >= size[0] - symsize:
			cursor[1] += symsize
			cursor[0] = 0

	display_tape(mcontext)
	mcontext.step()
	time.sleep(delay)

	pygame.display.flip()