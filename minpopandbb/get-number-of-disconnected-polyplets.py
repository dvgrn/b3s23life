# get-number-of-disconnected-polyplets.py
# find number of disconnected polyplets in a 2-state pattern

import golly as g

def hasneighbor(x,y):
  return ((x,y) in cells)

clist = g.getcells(g.getrect())
count = 0
cells = []
for i in range(0,len(clist),2):
  cells += [(clist[i],clist[i+1])]

while len(cells)>0:
  curcell = cells[-1]
  x, y = curcell
  
  # first fill in the neighbors list for the first cell in the new group
  # -- yes, this is unnecessary code duplication. It works, so I'm done.
  neighbors = []
  if hasneighbor(x-1,y-1): neighbors += [(x-1,y-1)]
  if hasneighbor(x-1,y): neighbors += [(x-1,y)]
  if hasneighbor(x-1,y+1): neighbors += [(x-1,y+1)]
  if hasneighbor(x,y-1): neighbors += [(x,y-1)]
  if hasneighbor(x,y+1): neighbors += [(x,y+1)]
  if hasneighbor(x+1,y-1): neighbors += [(x+1,y-1)]
  if hasneighbor(x+1,y): neighbors += [(x+1,y)]
  if hasneighbor(x+1,y+1): neighbors += [(x+1,y+1)]
  cells.remove(curcell)
  # g.note(str(neighbors) + "\nRemoved " + str(curcell))
  g.setcell(x,y,0)
  
  # now find neighbors of each cell in the neighbors list, until there are no more.
  while len(neighbors)>0:
    curcell = neighbors[-1]
    if curcell in cells: # neighbors will be added multiple times, so have to check against main list
      x, y = curcell
      if hasneighbor(x-1,y-1): neighbors += [(x-1,y-1)]
      if hasneighbor(x-1,y): neighbors += [(x-1,y)]
      if hasneighbor(x-1,y+1): neighbors += [(x-1,y+1)]
      if hasneighbor(x,y-1): neighbors += [(x,y-1)]
      if hasneighbor(x,y+1): neighbors += [(x,y+1)]
      if hasneighbor(x+1,y-1): neighbors += [(x+1,y-1)]
      if hasneighbor(x+1,y): neighbors += [(x+1,y)]
      if hasneighbor(x+1,y+1): neighbors += [(x+1,y+1)]
      g.setcell(x,y,0)
      cells.remove(curcell)
      # g.note(str(neighbors) + "\nRemoved " + str(curcell)) 
    else:
      pass
      # g.note("Cell " + str(curcell) + " was already removed.")
    # remove current cell from neighbors list, whether or not it was previously processed
    neighbors.remove(curcell)
  
  # neighbors list is empty -- add one to number of groups found
  count += 1
  g.show(str(count))
  g.update()  # remove this to make the run time a lot faster for large patterns

g.note("Number of groups found: " + str(count))
