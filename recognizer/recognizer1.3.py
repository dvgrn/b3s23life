# recognizer1.3.py
# Version 1.3:  fixed line 44 for Python3 compatibility (remove encode() to make it work in Python2)
# Version 1.2:  wrote populate-sample-library.py exporter script, created a sample archive
# Version 1.1:  added ability to read tickstorun and matchtype limitations from RLE file
# Version 1.0:  first working version

import golly as g
import hashlib
import os

libpath = g.getdir("data") + "recognizer-library/"
scriptFN = g.getdir("scripts") + "PatternBuildScript.py"
libraryFN = libpath + "library.txt"

xforms=[[1,0,0,1],[0,-1,1,0],[-1,0,0,-1],[0,1,-1,0],[0,1,1,0],[1,0,0,-1],[0,-1,-1,0],[-1,0,0,1]]
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
   m.update(str(cellsort(clist)).encode())
   return m.hexdigest()
   
# input is a TL/BR list of cells, the original phase of which
# was normalized to (0,0), plus an index into xforms[].
# output is a list containing [[outputlist], [xform]]
# where [outputlist] is transformed and normalized to put the
# first live cell at (0,0).  [xform] is the affine transform
# needed to move the original input to the normalized location
# (after running it T ticks to get to the appropriate phase).
def getorientation(clist, orientation):
   # g.note(str(orientation) + " :: " + str(xforms[orientation]) + " :: " + str(clist)) #################
   A, B, C, D = xforms[orientation]
   minx, miny = findTL(g.transform(clist, 0, 0, *xforms[orientation]))
   # return a pattern offset by the correct distance from the base pattern,
   # accounting for the location of the TL corner in the original phase --
   # -- but return the actual _pattern_ normalized to (0,0)!
   newlist = cellsort(g.transform(clist, -minx, -miny, A, B, C, D))
   return [newlist, [-minx, -miny, A, B, C, D]]

def getallorientations(name, clist, maxticks, matchtype = 0):
   names   = []
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
            names.append(name)
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
         if ticks>=8:
            g.show("No periodicity found within 8 ticks -- ending search.")
            nomatch = 0
            break
      else:
         # g.note(str(ticks) + " :: " + str(maxticks) + " :: " + str(ticks>=1)) #####################
         if ticks>=maxticks:
            nomatch = 0
            break # stop collecting patterns silently if a maximum has been specified
      clist = g.evolve(clist,1)

      x,y = findTLsorted(clist)
   return [names,uniques,xforms,orients,dticks]

def removecomments(s):
   temp = s + "#"
   return temp[:temp.find("#")].rstrip()

def writetoscript(patname, T, X, Y, orient):
   f = open(scriptFN, 'a')
   f.write("all += " + patname + ("[" + str(T) + "]" if T>0 else "") \
      + "(" + str(X) + "," + str(Y) \
      + ("," + xformnames[orient] if orient != 0 else "") + ")\n")
   f.close()

# should we update glife to work with multistate cell lists?
# need to convert to RLE at some point, but maybe a separate utility would work just as well.
# def writepatdef(patname, pat):
#    f = open(scriptFN, 'a') 
#    f.write(patname + " = pattern(" + str(pat) + ")\n")
#    f.close()

def writepatdef(patname, pat):
   with open(libpath + basename + ".rle", "r") as libfile:
      rle=libfile.readlines()
   rlestring=""
   for line in rle:
      if line[:1] in ['#', 'x', 'm']: continue
      rlestring+=line[:-1]
   x, y = findTL(g.parse(rlestring))
   f = open(scriptFN, 'a') 
   f.write(patname + " = pattern(g.parse('" + rlestring + "'," + str(-x)+","+str(-y)+"))\n")
   f.close()
   
def writetolibrary(patname, pat, ticks):
   g.store(pat, libpath + patname + ".rle")
   if ticks>0:
      f = open(libpath + patname + ".rle",'a')
      f.write("maxticks = " + str(ticks))
      f.close()

def matches(pat, x, y):
   for i in range(0, len(pat), 2):
      if g.getcell(pat[i]+x, pat[i+1]+y) % 2 == 0:
         return 0
#   bkg = getbackground(pat)
#   for i in range(0, len(bkg), 2):
#      if g.getcell(bkg[i]+x, bkg[i+1]+y) % 2 == 1:
#         return 0
   return 1

if g.getrule() != "B3/S23":
   g.exit("Please make sure the rule is set to standard B3/S23 Life before running this script.")

try: # initialize the output script -- #TODO: ask for an output filename
   f = open(scriptFN, 'w') 
   f.write("import golly as g\n")
   f.write("from glife import *\n")
   f.write("all = pattern()\n")
   f.close()
except:
   g.exit("Unable to initialize " + scriptFN)

nomatch = 1
namelist = []
patlist = []
xformlist = []
orientlist = []
ticklist = []

f = open(libraryFN, 'r') 
patnames=f.readlines()
f.close()

matchtype = 0

for name in patnames:
   tickstorun = 0
   basename = removecomments(name)
   temp = basename.split(" ")
   if len(temp)==2: basename, tickstorun = temp
   if len(temp)==3: basename, tickstorun, matchtype = temp
   base = g.load(libpath + basename + ".rle")
   # oddly, g.load() doesn't pay attention to CXRLE -- it just
   #  loads the pattern at (0,0).  So we have to normalize anyway...!
   offx, offy = findTL(base)
   base = g.transform(base, -offx, -offy)  # move upper left live cell to (0,0)
   writepatdef(basename, base) #TODO:  write script in two phases, including only patterns actually used
   g.show("Loading pattern '" + basename + "' into memory.")
   n,p,x,o,t = getallorientations(basename, base, int(tickstorun), int(matchtype))
   namelist+=n
   patlist+=p
   xformlist+=x
   orientlist+=o
   ticklist+=t

remainder = g.getcells(g.getrect())
while len(remainder):
   matchflag = 0
   for index in range(len(patlist)):
      pat = patlist[index]
      if g.getkey() == "q": g.exit()
      TLx, TLy = findTLsorted(remainder) # TODO:  think about optimizing this to work from getrect() instead of cell list
      matchflag = matches(pat, TLx, TLy)
      if matchflag:
         xf=xformlist[index] # TODO:  still have to fix all this [index] silliness... ##################
         writetoscript(namelist[index], ticklist[index], TLx+xf[0], TLy+xf[1], orientlist[index])
         # remove the matched pattern from the universe
         g.putcells(pat, TLx, TLy, 1, 0, 0, 1, "xor")
         g.show("Found " + namelist[index] + " at " + str(TLx+xf[0]) + "," + str(TLy+xf[1]) + ", orientation " + str(index))
         g.update()
         nomatch = 0
         break
   if matchflag == 0:
      writepatdef("remainder",remainder)
      g.exit("Upper left ON cell didn't match any patterns in the library.  Register a new subpattern.")
   remainder = g.getcells(g.getrect())
f = open(scriptFN, 'a')
f.write("g.new(\"Script-Output\")\n")
f.write("all.put()\n")
f.write("g.fit()\n")
f.close()
g.update()
g.note("Script has been written to " + scriptFN + ".")
   
   
