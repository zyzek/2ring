import machines

from os.path import relpath
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pygame, sys, os, time
from pygame.locals import *

imgdir = "img/"
symdir = "img/symbols/"

white = (255, 255, 255)
black = (0, 0, 0)
gridcolour = (0, 20, 40)
gridhighlight = (0, 30, 45)
machine_cols = {}

clock = None
running = True
framerate = 60.0
maxsimrate = 2000
simrate = 120.0
timestep = 1000.0/simrate
elapsed = 0
last_time = 0
accumulator = 0

font = None
symsize = 16
symbols = {}
uisize = 32
fontsize = uisize//2
iconsize = (3*uisize)//4
uiicons = {}
size = (800, 600)
symbuffer = 0
origin = (size[0]//3 - (size[0]//3)%symsize, size[1]//3 - (size[1]//3)%symsize)
tileoffset = [0,0]
screen = None
display_machines = True

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
	global screen, symbols, clock, font, mcontext, last_time
	Tk().withdraw()
	pygame.init()

	mcontext = initcontext
	mcontext.checkpoint()

	clock = pygame.time.Clock()
	last_time = pygame.time.get_ticks()
	font = pygame.font.Font(None, fontsize)

	screen = pygame.display.set_mode(size, pygame.RESIZABLE)
	reload_sym_images()

	uiicons["runrect"] = pygame.Rect(screen.get_size()[0] - iconsize, 0, iconsize, iconsize)
	uiicons["runimg"] = pygame.transform.smoothscale(pygame.image.load(imgdir + "running.bmp"), (iconsize,iconsize))
	uiicons["stopimg"] = pygame.transform.smoothscale(pygame.image.load(imgdir + "stopped.bmp"), (iconsize,iconsize))
	uiicons["filerect"] = pygame.Rect(screen.get_size()[0] - iconsize*2, 0, iconsize, iconsize)
	uiicons["fileimg"] = pygame.transform.smoothscale(pygame.image.load(imgdir + "file.png"), (iconsize,iconsize))

def reload_sym_images():
	for filename in os.listdir(symdir):
		key = filename[:-4]
		if key.endswith("_"):
			key = key[:-1]

		symbols[key] = pygame.transform.smoothscale(pygame.image.load(symdir + filename), (symsize-symbuffer,symsize-symbuffer))

def get_sym_img(symbol):
	try:
		return symbols[symbol]
	except KeyError:
		try:
			return symbols[symdict[symbol]]
		except KeyError:
			return symbols["ERR"]

def draw_grid():
	for i in range(screen.get_size()[0]//symsize + 1):
		pygame.draw.line(screen, gridcolour, (i*symsize - 1, 0), (i*symsize - 1, screen.get_size()[1]), 2)
	for i in range(screen.get_size()[1]//symsize + 1):
		pygame.draw.line(screen, gridcolour, (0, i*symsize - 1), (screen.get_size()[0], i*symsize - 1), 2)

	for i in range(-1, screen.get_size()[0]//(symsize*5) + 1):
		for j in range(-1, screen.get_size()[1]//(symsize*5) + 1):
			pygame.draw.circle(screen, gridhighlight, ((5*i + tileoffset[0]%5)*symsize + 1, (5*j+tileoffset[1]%5)*symsize + 1), 2)

def display_tape():
	draw_grid()

	for point in mcontext.tape:
		coords = (origin[0] + (tileoffset[0] + point[0])*symsize + symbuffer,
				  origin[1] + (tileoffset[1] + point[1])*symsize + symbuffer)
		screen.blit(get_sym_img(mcontext.tape[point]), coords)

	if display_machines:
		m = 0
		for machine in mcontext.running[::-1]:
			mrect = pygame.Rect(origin[0] + (tileoffset[0] + machine.pos[0])*symsize,
								origin[1] + (tileoffset[1] + machine.pos[1])*symsize,
								symsize, symsize)
			pygame.draw.rect(screen, machine.color, mrect, 2)

			mrect = pygame.Rect(m*110 + 2, screen.get_size()[1]-(uisize+5), 100, uisize)
			pygame.draw.rect(screen, black, mrect, 0)
			screen.blit(font.render(machine.path.split("/")[-1], 1, white), (m*110 + 5, screen.get_size()[1]-uisize))
			screen.blit(font.render(str(machine.pos) + " " + str(machine.state), 1, white), (m*110 + 5, screen.get_size()[1]-uisize//2))
			pygame.draw.rect(screen, machine.color, mrect, 2)

			m += 1


def display_UI():
	screen.blit(font.render("Target sim rate: " + str(int(simrate) if simrate < maxsimrate else "MAX") + " ticks/s", 1, white), (0,0))
	screen.blit(font.render("Elapsed ticks: " + str(elapsed), 1, white), (0, fontsize))
	screen.blit(uiicons["runimg"] if running else uiicons["stopimg"], uiicons["runrect"])
	screen.blit(uiicons["fileimg"], uiicons["filerect"])

def load_machine_dialog():
	try:
		running = False
		tileoffset[0] = tileoffset[1] = elapsed = 0
		mcontext = machines.MachineContext(machines.Plane())
		mcontext.create_machine(relpath(askopenfilename()))
	except:
		pass

def handle_events():
	global running, simrate, timestep, display_machines, mcontext, symsize, elapsed

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if uiicons["runrect"].collidepoint(event.pos):
					running = not running
				elif uiicons["filerect"].collidepoint(event.pos):
					load_machine_dialog()

		if event.type == pygame.KEYDOWN:
			if event.key == K_EQUALS:
				simrate = simrate*1.3 if simrate < maxsimrate else simrate
				timestep = 1000.0/simrate
			elif event.key == K_MINUS:
				simrate = simrate/1.3 if simrate > 1 else simrate
				timestep = 1000.0/simrate
			elif event.key == K_LEFTBRACKET:
				symsize = symsize//2 if symsize >= 4 else symsize
				reload_sym_images()
			elif event.key == K_RIGHTBRACKET:
				symsize = symsize*2 if symsize < 64 else symsize
				reload_sym_images()
			elif event.key == K_ESCAPE:
				sys.exit()
			elif event.key == K_RETURN:
				running = not running
			elif event.key == K_UP:
				tileoffset[1] += 64//symsize
			elif event.key == K_DOWN:
				tileoffset[1] -= 64//symsize
			elif event.key == K_RIGHT:
				tileoffset[0] -= 64//symsize
			elif event.key == K_LEFT:
				tileoffset[0] += 64//symsize
			elif event.key == K_s:
				running = True
				s_step()
				render()
				running = False
			elif event.key == K_m:
				display_machines = not display_machines
			elif event.key == K_r:
				mcontext = mcontext.restore()
				tileoffset[0] = tileoffset[1] = elapsed = 0
			elif event.key == K_f:
				load_machine_dialog()


def render():
	handle_events()	
	screen.fill(black)
	display_tape()
	display_UI()
	pygame.display.flip()
	#pygame.image.save(screen, "screenshot/" + str(elapsed) + ".png")


def s_step():
	global elapsed, running, mcontext

	if running:
		mcontext.step()
		elapsed += 1


def run():
	global timestep, framerate, last_time, current_time, accumulator

	while True:
		current_time = pygame.time.get_ticks()
		accumulator += current_time - last_time
		last_time = current_time

		while accumulator >= timestep:
			s_step()
			accumulator -= timestep

		render()
		clock.tick(framerate)	