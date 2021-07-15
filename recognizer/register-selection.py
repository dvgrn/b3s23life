import golly as g
import hashlib
import os

libpath = g.getdir("data") + "recognizer-library/"
if not os.path.isdir(libpath): os.makedirs(libpath)

# for filename in os.listdir(libpath):
#    g.note(filename)
# g.exit

oldsavexrle = g.setoption("savexrle", 1) 
xformlist=[[1,0,0,1],[0,-1,1,0],[-1,0,0,-1],[0,1,-1,0],[0,1,1,0],[1,0,0,-1],[0,-1,-1,0],[-1,0,0,1]]
xformnames = ["identity","rcw","flip","rccw","swap_xy","flip_y","swap_xy_flip","flip_x"]  # for glife script
g.setrule("B3/S23")

# returns a cell list sorted into TL/BR order
def cellsort(clist):
   return g.evolve(clist, 0)

def findTL(clist):
   return findTLsorted(cellsort(clist))

# version of findTL() for cell lists already known to be in TL/BR order
def findTLsorted(slist):
   return (slist[0],slist[1])

def getbackground(clist):
   g.setrule("B12345678/S")
   background = g.evolve(clist, 1)
   g.setrule("B3/S23")
   return background

# Calls cellsort() to make sure the input is normalized --
# first live cell in upper left is (0,0), and
# cells are sorted in TL/BR order
# Not using Golly's native hash() method because
# the cell list would have to be pasted into a layer somewhere
# (golly.hash() takes a rectangle as input, not a cell list)
def gethash(clist):
   m = hashlib.md5()
   m.update(str(cellsort(clist)))
   return m.hexdigest()
   
# input is a TL/BR list of cells, the original phase of which
# was normalized to (0,0), plus an index into xformlist[].
# output is a list containing [[outputlist], [xform]]
# where [outputlist] is transformed and normalized to put the
# first live cell at (0,0).  [xform] is the affine transform
# needed to move the original input to the normalized location
# (after running it T ticks to get to the appropriate phase).
def getorientation(clist, orientation):
   A, B, C, D = xformlist[orientation]
   minx, miny = findTL(g.transform(clist, 0, 0, *xformlist[orientation]))
   # return a pattern offset by the correct distance from the base pattern,
   # accounting for the location of the TL corner in the original phase --
   # -- but return the actual _pattern_ normalized to (0,0)!
   newlist = cellsort(g.transform(clist, -minx, -miny, A, B, C, D))
   return [newlist, [-minx, -miny, A, B, C, D]]

def getallorientations(clist, maxticks, matchtype = 0):
   uniques = []
   xforms  = []
   uhashes = []
   orients = []
   dticks  = []
   ticks = 0

   rangemax = (8 if matchtype == 0 else matchtype) # 1 (no rot/ref) or 4 (rotation only) are reasonable
   nomatch = 1
   while nomatch: # check next generation until a repeat occurs in orientation 1
      for i in range(rangemax): # TODO:  invent a structure to avoid having to use indexes like this
         pat, xform = getorientation(clist, i)
         h = gethash(pat)
         if uhashes.count(h)==0:
            uniques.append(pat)
            uhashes.append(h)
            xforms.append(xform)
            orients.append(i)
            dticks.append(ticks)
         else:
            if i==0:
               nomatch = 0 # if we've already seen the first phase, we've seen them all from here on out.
               break       # (for other phases the duplication might be due to symmetry, so we try them all)
      if nomatch == 0:  break # TODO:  this is silly -- find a better structural way to do this
      ticks += 1
      if maxticks<=0:
         if ticks>=512:
            g.note("No periodicity found within 512 ticks -- ending search.")
            nomatch = 0
            break
      else:
         g.note(str(ticks) + " :: " + str(maxticks) + " :: " + str(ticks>=1)) #####################
         if ticks>=maxticks:
            nomatch = 0
            break # stop collecting patterns silently if a maximum has been specified
      clist = g.evolve(clist,1)

      x,y = findTLsorted(clist)
   return [uniques,xforms,orients,dticks]

# should we update glife to work with multistate cell lists?
# need to convert to RLE at some point, but maybe a separate utility would work just as well.
def writepatdef(patname, pat):
   f = open(scriptFN, 'a') 
   f.write(patname + " = pattern(" + str(pat) + ")\n")
   f.close()

def writetolibrary(patname, pat, ticks):
   g.store(pat, libpath + patname + ".rle")
   if ticks>0:
      f = open(libpath + patname + ".rle",'a')
      f.write("maxticks = " + str(ticks))
      f.close()
   
if g.getrule() != "B3/S23":
   g.exit("Please make sure the rule is set to standard B3/S23 Life before running this script.")

rect = g.getselrect()
if len(rect) == 0:
   rect = g.getrect()
if len(g.getcells(rect)) == 0:
   rect=g.getrect()
if len(rect) == 0:
   g.exit("The universe is empty!")
base = g.getcells(rect)
if findTL(base)==():
   g.exit("No live cells found.")
prompt = "Enter name for selected object\nand optional ticks to run and\nmatch type (space delimited):"
s = prompt
tickstorun = 0
matchtype = 0
while 1:
   basename = g.getstring(s)
   temp = basename.split(" ")
   if len(temp)==2: basename, tickstorun = temp
   if len(temp)==3: basename, tickstorun, matchtype = temp
   if os.path.exists(libpath + basename + ".rle"):
      s = "That name is already defined in\n" + libpath + prompt + "\n\n"
   else:
      break
offx, offy = findTL(base)
base = g.transform(base, -offx, -offy)  # move upper left live cell to (0,0)
writetolibrary(basename, base, tickstorun)
f = open(libpath+"library.txt", 'a')
f.write(basename + "\n")
f.close()
g.exit("")

# without g.exit() above, the script looks for the next pattern that's not in the library
# -- let's not do that in version 1.2 -- too confusing

patlist,xformlist,orientlist,ticklist = getallorientations(base, int(tickstorun), int(matchtype))

remainder = g.getcells(g.getrect())
while len(remainder)>1:
   TLx, TLy = findTLsorted(remainder)
   nomatch = 1
   while nomatch:
      for index in range(len(patlist)):
         pat = patlist[index]
         if g.getkey() == "q": g.exit()
         patmatch = 1
         for i in range(0, len(pat), 2):
            if g.getcell(pat[i]+TLx, pat[i+1]+TLy) % 2 == 0:
               patmatch = 0
               break
         if patmatch:
            bkg = getbackground(pat)

            for i in range(0, len(bkg), 2):
               if g.getcell(bkg[i]+TLx, bkg[i+1]+TLy) % 2 == 1:
                  patmatch = 0
                  break
         if patmatch:
            xf=xformlist[index]
            g.putcells(pat, TLx, TLy, 1, 0, 0, 1, "xor")
            nomatch = 0
            break
      if nomatch:
         g.exit("Upper left ON cell didn't match any patterns in the library.  Register a new subpattern.")
   remainder = g.getcells(g.getrect())
g.setoption("savexrle", oldsavexrle) 

