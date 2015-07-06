import machines, tapes
import pygame, sys, os, time
from pygame.locals import *

clock = None
font = None

running = True
framerate = 60.0
symsize = 16
symbols = {}
size = (800, 600)
origin = (size[0]/3, size[1]/3)
tileoffset = [0,0]
screen = None 

symdict = {}
symdict["*"] = "star"
symdict["<"] = "langbrack"
symdict[">"] = "rangbrack"
symdict["│"] = "vline"
symdict["─"] = "hline"
symdict["┐"] = "ldcorn"
symdict["┌"] = "rdcorn"
symdict["└"] = "rucorn"
symdict["┘"] = "lucorn"
symdict["'"] = "quote"
symdict['"'] = "dquote"
symdict["?"] = "qmark"
symdict[";"] = "semicolon"
symdict["|"] = "pipe"

def init():
	global screen, symbols, clock, font 
	pygame.init()

	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 20)

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
		coords = (origin[0] + (tileoffset[0] + point[0])*symsize,
				  origin[1] + (tileoffset[1] + point[1])*symsize)
		screen.blit(get_sym_img(mcontext.tape[point]), coords)

def handle_events():
	global tileoffset, framerate, running

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == K_EQUALS:
				framerate *= 1.1
			elif event.key == K_MINUS:
				framerate /= 1.1
			elif event.key == K_ESCAPE:
				sys.exit()
			elif event.key == K_RETURN:
				running = not running
			elif event.key == K_UP:
				tileoffset[1] += 1
			elif event.key == K_DOWN:
				tileoffset[1] -= 1
			elif event.key == K_RIGHT:
				tileoffset[0] -= 1
			elif event.key == K_LEFT:
				tileoffset[0] += 1

def step(mcontext):
	global running, screen, size, symsize, framerate, clock, font

	handle_events()	

	screen.fill((0,0,0))
	display_tape(mcontext)
	screen.blit(font.render("Target framerate: " + str(int(framerate)), 1, (200, 200, 200)), (0,0))
	pygame.display.flip()

	if running:
		mcontext.step()

	clock.tick(framerate)