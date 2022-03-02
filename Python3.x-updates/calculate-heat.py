# Golly Python script
# Written by Nathaniel Johnston
# March 28, 2009
# Python 3.x udates by Book, March 1, 2022
# https://conwaylife.com/forums/viewtopic.php?p=142312#p142312

''' Calculate the heat of the current oscillator/spaceship '''       

from glife import getstring, validint 
import golly as g

def chunks(l,w):
    for i in range(0, len(l), 2):
        yield l[i]+(w*l[i+1])

if g.empty(): g.exit("The pattern is empty.")
s = g.getstring("Enter the period:","", "Heat calculator")

if not validint(s): 
  g.exit('Bad number: %s' % s)
numsteps = int(s)
if numsteps < 2:
  g.exit('Period must be at least 2.')

g.show('Processing...')

heat = 0;
maxheat = 0;
minheat = int(9*g.getpop());

for i in range(0, numsteps):
  bb = g.getrect()
  clist = list(chunks(g.getcells(bb), bb[2]+2))
  g.run(1)
  dlist = list(chunks(g.getcells(g.getrect()), bb[2]+2))
  theat = (len(clist)+len(dlist)-2*len([x for x in set(clist).intersection( set(dlist) )]))
  heat += theat
  maxheat = max(theat, maxheat)
  minheat = min(theat, minheat)

g.show('Heat: %.4f, Max change: %d, Min change: %d' % ((float(heat)/numsteps), maxheat, minheat))
