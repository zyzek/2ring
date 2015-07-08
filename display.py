import machines, tapes
import pygame, sys, os, time
from pygame.locals import *

imgdir = "img/"
symdir = "img/symbols/"

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

machine_cols = {}

clock = None
font = None

running = True
framerate = 60.0
elapsed = 0
symsize = 16
symbols = {}
uisize = 32
uiicons = {}
size = (800, 600)
origin = (size[0]/3, size[1]/3)
tileoffset = [0,0]
screen = None 

mcontext = None


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

def init(initcontext):
	global screen, symbols, clock, font, mcontext 
	pygame.init()

	mcontext = initcontext
	mcontext.checkpoint()

	clock = pygame.time.Clock()
	font = pygame.font.Font(None, uisize//2)

	screen = pygame.display.set_mode(size, pygame.RESIZABLE)
	for filename in os.listdir(symdir):
		key = filename[:-4]
		if key.endswith("_"):
			key = key[:-1]

		symbols[key] = pygame.transform.smoothscale(pygame.image.load(symdir + filename), (symsize,symsize))

	uiicons["runrect"] = pygame.Rect(screen.get_size()[0] - uisize, 0, uisize, uisize)
	uiicons["runimg"] = pygame.transform.smoothscale(pygame.image.load(imgdir + "running.bmp"), (uisize,uisize))
	uiicons["stopimg"] = pygame.transform.smoothscale(pygame.image.load(imgdir + "stopped.bmp"), (uisize,uisize))

def get_sym_img(symbol):
	try:
		return symbols[symbol]
	except KeyError:
		try:
			return symbols[symdict[symbol]]
		except KeyError:
			return symbols["ERR"]

def display_tape():
	global mcontext
	for point in mcontext.tape:
		coords = (origin[0] + (tileoffset[0] + point[0])*symsize,
				  origin[1] + (tileoffset[1] + point[1])*symsize)
		screen.blit(get_sym_img(mcontext.tape[point]), coords)

	for machine in mcontext.running:
		mrect = pygame.Rect(origin[0] + (tileoffset[0] + machine.pos[0])*symsize,
							origin[1] + (tileoffset[1] + machine.pos[1])*symsize,
							symsize, symsize)
		pygame.draw.rect(screen, machine.color, mrect, 2)


def display_UI():
	global font, framerate, elapsed

	screen.blit(font.render("Target framerate: " + str(int(framerate) if framerate < 1000 else "MAX"), 1, white), (0,0))
	screen.blit(font.render("Elapsed ticks: " + str(elapsed), 1, white), (0, uisize//2))
	screen.blit(uiicons["runimg"] if running else uiicons["stopimg"], uiicons["runrect"])

def handle_events():
	global tileoffset, framerate, running, mcontext

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if uiicons["runrect"].collidepoint(event.pos):
					running = not running

		if event.type == pygame.KEYDOWN:
			if event.key == K_EQUALS:
				framerate = framerate*1.3 if framerate < 1000 else framerate
			elif event.key == K_MINUS:
				framerate = framerate/1.3 if framerate > 1 else framerate
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
			elif event.key == K_r:
				print("restoring")
				mcontext.restore()


def step():
	global running, screen, size, symsize, framerate, clock, elapsed, mcontext

	handle_events()	

	screen.fill(black)
	display_tape()
	display_UI()
	pygame.display.flip()

	if running:
		mcontext.step()
		elapsed += 1

	if framerate < 1000:
		clock.tick(framerate)