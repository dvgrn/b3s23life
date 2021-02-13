# glider_destruction_v2_Python3.py
# Enter a pattern and this script will try to find a single-glider destruction of it.
#
# Recently added features:
# -When user presses a key, copy result to clipboard instead of ending program to show it
# -Terminates script when periodicity is detected
#
# Ways to improve this script:
# -Use the bounding diamond instead of the bounding box
# -If pattern is symmetrical, not check redundant collisions
# -Change boxstatus and popstatus into a list containing a list or tuple and a tuple, and a list containing a number and a tuple respectively.
# -Find minimum population for 1000 generations instead of population after 1000 generations

import golly as g
import functools
from operator import mul

glider = [[-1, -2, 0, -1, -2, 0, -1, 0, 0, 0], [-2, -2, -1, -1, 0, -1, -2, 0, -1, 0], [-1, -2, -3, -1, -1, -1, -2, 0, -1, 0], [-3, -2, -1, -2, -2, -1, -1, -1, -2, 0]]
boxstatus = ([10 ** 9, 10 ** 9], 0, 0, [0, 0]) #(dummy values) box_size, pattern_pos, glider_phase, [glider_x, glider_y]
popstatus = (int(g.getpop()) + 5, 0, 0, [0, 0])

# In this and the following function, "num" represents one of the eight possible transformations of the pattern, encoded as a 3-bit binary number.
# The first bit represents whether the pattern has been turned upside down from its original orientation,
# the second bit represents whether it has been rotated clockwise by 90 degrees,
# and the third bit represents whether it has been flipped about the x-axis.
def form(celllist, num):
	if num not in range(8):
		return celllist
	if num >= 4:
		celllist = g.transform(celllist, 0, 0, -1, 0, 0, -1)
		num -= 4
	if num >= 2:
		celllist = g.transform(celllist, 0, 0, 0, 1, -1, 0)
		num -= 2
	if num >= 1:
		celllist = g.transform(celllist, 0, 0, -1, 0, 0, 1)
	return celllist

def deform(celllist, num):
	if num not in range(8):
		return celllist
	if num % 2 == 1:
		celllist = g.transform(celllist, 0, 0, -1, 0, 0, 1)
	num = num / 2
	if num % 2 == 1:
		celllist = g.transform(celllist, 0, 0, 0, -1, 1, 0)
	num = num / 2
	if num % 2 == 1:
		celllist = g.transform(celllist, 0, 0, -1, 0, 0, -1)
		num -= 4
	return celllist

def boxform(rect, num):
	newrect = list(rect) #kludge
	if num not in range(8):
		return newrect
	if num >= 4:
		newrect[0] = -newrect[0] - newrect[2] + 1
		newrect[1] = -newrect[1] - newrect[3] + 1
		num -= 4
	if num >= 2:
		newrect = [newrect[1], -newrect[0] - newrect[2] + 1, newrect[3], newrect[2]]
		num -= 2
	if num >= 1:
		newrect[0] = -newrect[0] - newrect[2] + 1
	return newrect

def putcells_and_fit(celllist):
	g.putcells(celllist)
	g.fit()

def trygliders(ginfo):
	gdistance = ginfo // 4
	phase = ginfo % 4
	bstatus = boxstatus
	pstatus = popstatus
	for num in range(8):
		tlist = form(celllist, num)
		rect = boxform(fullrect, num)
		g.new('')
		g.putcells(tlist)
		gx = rect[0] - 3 - gdistance
		gy = rect[1] - 3 - gdistance
		for w in range(rect[2] + 5):
			g.new('')
			g.putcells(tlist)
			g.putcells(glider[phase], gx + w, gy)
			g.fit()
			g.update()
			for gen in range(1000):
				g.run(1)
				if int(g.getpop()) <= 2:
					g.new('')
					g.show("Found clean glider destruction.")
					status = 0, num, phase, [gx + w, gy]
					putcells_and_fit(result(celllist, status))
					g.exit()
			box = g.getrect()[2:]
			# Checking the bounding box size and population against the current lowest found.
			if functools.reduce(mul, box) < functools.reduce(mul, bstatus[0]):
				bstatus = (box, num, phase, [gx + w, gy])
			pop = int(g.getpop())
			if pop < pstatus[0]:
				pstatus = (pop, num, phase, [gx + w, gy])
			# Show results if the user presses certain keys
			event = g.getevent()
			if event.startswith("key x"):
				g.new('')
				put_result_pair(celllist, bstatus, pstatus)
				g.select(g.getrect())
				g.copy()
				g.select([])
				g.note("Minimum bounding box and population collisions copied to clipboard.")
			if event.startswith("key q"):
				g.new('')
				g.show("Search stopped.")
				put_result_pair(celllist, bstatus, pstatus)
				g.fit()
				g.exit()
			g.show("Searching for a 1-glider destruction... press <x> to copy minimum bounding box and population results to clipboard; press <q> to quit. Stats: minimum bounding box %dx%d, minimum population %d" % (bstatus[0][0], bstatus[0][1], pstatus[0]))
	return bstatus, pstatus

def result(celllist, status):
	return celllist + deform(g.transform(glider[status[2]], status[3][0], status[3][1]), status[1])

def put_result_pair(celllist, bstatus, pstatus):
	g.putcells(result(celllist, bstatus) + g.transform(result(celllist, pstatus), 3*pattrect[2], 0))

def bounding_box_union(bbox1, bbox2):
	bbox_union = []
	if bbox2[0] > bbox1[0]:
		bbox_union.append(bbox1[0])
	else:
		bbox_union.append(bbox2[0])
	if bbox2[1] > bbox1[1]:
		bbox_union.append(bbox1[1])
	else:
		bbox_union.append(bbox2[1])
	if bbox2[0] + bbox2[2] > bbox1[0] + bbox1[2]:
		bbox_union.append(bbox2[0] + bbox2[2] - bbox_union[0])
	else:
		bbox_union.append(bbox1[0] + bbox1[2] - bbox_union[0])
	if bbox2[1] + bbox2[3] > bbox1[1] + bbox1[3]:
		bbox_union.append(bbox2[1] + bbox2[3] - bbox_union[1])
	else:
		bbox_union.append(bbox1[1] + bbox1[3] - bbox_union[1])
	return bbox_union

glidersexist = (g.evolve([-1, -2, 0, -1, -2, 0, -1, 0, 0, 0], 4) == [0, -1, 1, 0, -1, 1, 0, 1, 1, 1])
if not glidersexist:
	g.exit("Please choose a rule where gliders exist.")

# pattrect is the bounding box of the initial generation
# fullrect is the union of the bounding boxes of all the generations up to the current (specified by the variable "info" for complicated reasons)
pattrect = g.getrect()
fullrect = pattrect
celllist = g.getcells(pattrect)
currlist = celllist
gen_status_list = []
info = 0

g.addlayer()
while True:
	for tup in gen_status_list:
		if tup[0] == currlist:
			if tup[1] == fullrect:
				g.new('')
				g.show("Search complete. No glider destruction found. Minimum bounding box and population results given.")
				put_result_pair(celllist, boxstatus, popstatus)
				g.fit()
				g.exit()
	
	boxstatus, popstatus = trygliders(info)
	info += 1
	
	gen_status_list.append((currlist, fullrect))
	
	g.new('')
	currlist = g.evolve(currlist, 1)
	g.putcells(currlist)
	fullrect = bounding_box_union(fullrect, g.getrect())
