# ticker-maker-p46-Python3.py
# Golly Python script. Written by PM 2Ring, March 2009.
# Update to Python3 and RLE format that doesn't work with current Golly fixed by dvgrn, June 2022.

''' Create a 'bitmap printer', based on the golly logo ticker.
  Uses the current selection as the bitmap source.
 '''

import golly
from glife import * 

def get_bitmap():
  ''' Get current selection & turn it into a bitmap. '''  
  selrect = golly.getselrect()
  if len(selrect) == 0: golly.exit("There is no selection, aborting.")
    
  #Get bitmap size   
  w, h = selrect[2:]
  #Adjust width, so it's in the form of 4m+1, m>=1 
  w = max(w + 2, 4) // 4 * 4 + 1 
  #w += 4  #Padding
  #print w
  
  #Initialize empty bitmap
  row = w * [0]
  bm = [row[:] for i in range(h)]

  #Populate bitmap with cell data    
  u, v = selrect[:2]
  cells = golly.getcells(selrect)  
  cellsxy = [(cells[i] - u, cells[i+1] - v) for i in range(0, len(cells), 2)]
  for x, y in cellsxy:
    bm[y][x] = 1  
  return bm

def gliders():
  ''' Glider loop parts '''  
  #Basic glider, pointing south-west
  g0 = pattern('bob$o$3o!')
  glist = [g0.evolve(i) for i in range(4)]

  #Required glider configurations,
  #aligned so top left corner of bounding box is at 0,0  
  g0y   = glist[0](0, 2, flip_y)
  g0xy  = glist[0](2, 2, flip)
  g1    = glist[1](0, -1)  
  g2y   = glist[2](0, 3, flip_y)
  g2xy  = glist[2](2, 3, flip)
  g3    = glist[3](1, -1)  
  g3x   = glist[3](1, -1, flip_x)

  #Order as used in Line Makers. 0, 1, (2, 1), 3, 4, 6, (5, 6)   
  gg = [g3x, g0xy, g2xy, g0y, g2y, g3, g1]  
  #for i,glider in enumerate(gg): glider.put(10*i, 0)
  return gg    
   
def linemaker():
  ''' Line Maker parts '''
  LMTop = pattern('''8bo$9bo3bo$2o2b2o8bo12b2o$2o2bo5b2o2bo12b2o$4bobo5b2o$5b2o3b3o2$5b2o3b
  3o$4bobo5b2o$4bo5b2o2bo$4b2o8bo$9bo3bo$8bo2$37b2o$37b2o7$30b3o3b3o$30b
  o2bobo2bo$29bo3bobo3bo$29b4o3b4o$30bo7bo7$37bo$36b3o$35bo3bo$35b2ob2o$
  35b2ob2o2$35b2ob2o$35b2ob2o$30b2o3bo3bo$30b2o4b3o$37bo!''')
     
  LMBase = pattern('''8b2o$8b2o13$b2o5b2o$o2bo3bo2bo$bo2bobo2bo$4bobo$2b3ob3o$3o5b3o$2o7b2o$
  2o7b2o$bob2ob2obo$b3o3b3o$2bo5bo$10bo5bo$9b3o3b3o$9bob2ob2obo$8b2o7b2o
  $8b2o7b2o$8b3o5b3o$10b3ob3o$12bobo$9bo2bobo2bo$8bo2bo3bo2bo$9b2o5b2o
  10$28b2o$28b2o2$16b2o$16b2o8$87b2o$30bo3bo52b2o$30bo3bo3$27b2obo3bob2o
  $28b3o3b3o43b3o3b3o$29bo5bo44bo2bobo2bo$79bo3bobo3bo$80bo2bobo2bo$82bo
  3bo$80b2o5b2o$79b3o5b3o$79b3o5b3o2$35b2o$35b2o2$80b3o$80b3o$79b5o$78b
  2o3b2o$78b2o3b2o4$78b2o3b2o$78b2o3b2o2b2o$79b5o3b2o$80b3o$80b3o!''')
  return LMTop, LMBase 

def dmprinter(pdy, copies=1):
  ''' Generate & display a dot matrix printer for named bitmap pattern ''' 
  #Horizontal pixel separation between Line Makers. minimum = 4
  LMsx = 4 
  
  #Horizontal distance between bitmap pixels. Constant, due to LineMaker period 
  pdx = 23         
    
  #Distance between Line Makers
  LMdx, LMdy = -LMsx * pdx, pdy
  
  #Get Line Maker parts  
  LMTop, LMBase = linemaker() 
  
  #Eaters facing south-east & north-east 
  eaterSE = pattern('2o$bo$bobo$2b2o!')
  eaterNE = eaterSE(0, 10, flip_y)
  y = 74
  eaters = (eaterNE(0, y), eaterSE(0, y))

  #Get bitmap pattern from current selection.
  bm = get_bitmap()
  
  #Make printer in a new layer 
  golly.duplicate()
  golly.setoption("syncviews", False) 

  #Build new window title from old  
  title = golly.getname().split('.')[0]
  title = '%s_Printer [%d] v0.9' % (title, pdy)  
  golly.new(title)  
  
  #Make sure we're using the standard Life generation rule
  golly.setrule("B3/S23")
  
  #Bitmap dimensions. Width MUST be of form 4m+1, for m >=1 
  bmheight = len(bm)   
  bmwidth = len(bm[0])     
  mid = bmheight // 2  
    
  loopw = (bmwidth - 5) // 4  
  loopm = pdx * loopw  
  
  #Glider configurations list
  gg = gliders()

  #Glider loop ordering
  gnum = [0, 1] + loopw * [2, 1] + [3, 4, 6] + loopw * [5, 6]

  #Basic glider offsets. Sorry about all the magic numbers :)  
  gdeltas = [(24, 34), (34, 44), (22, 55), (44, 32), (33, 20), (8, 31), (20, 20)]
  
  #Actual glider offsets
  a = list(range(loopw + 1))
  t = [i * pdx for i in a for j in (0, 1)]
  tr = t[:]; tr.reverse()
  goff = (t + 2*[loopm] + tr)[:-1] 
  
  #Eater horizontal displacement. Must be opposite parity to LMsx
  #bmwidth muliplier determines number of copies visible 'outside' printer.
  #4 complete columns are actually visible 'inside' printer.
  eX = (bmheight + 1) * LMdx - (copies * bmwidth - 4) * pdx  
  #Adjust parity
  eX = (LMsx + 1) % 2 + eX // 2 * 2 

  def buildLM():
    ''' Build a complete LineMaker '''
    #Build glider loop. (jj, ii) are bitmap coords 
    gloop = pattern()
    for j in range(bmwidth):
      jj = bmwidth - 1 - (j + LMsx * io) % bmwidth
      
      #Is there a pixel at this location?
      if not bm[ii][jj]: 
        continue

      #Glider config number & offset      
      num, off = gnum[j], goff[j]
      x, y = gdeltas[num]
      
      #Add glider to the loop
      gloop += gg[num](x + off, y - off)   

    #Only put LineMaker if glider loop isn't empty
    if len(gloop) > 0:
      (LMFull + gloop).put(Lx, Ly, trans)
    #Add an eater to limit bitmap length. Could be in the 
    #if block, but it looks neater with all eaters present.  
    eaters[(ii + it) % (1 + LMsx%2)].put(eX, Ly, trans)        

  #Assemble LineMaker
  Tdx, Tdy = 18 + loopm, 2 - loopm  
  LMFull = LMBase + LMTop.translate(Tdx, Tdy)
      
  transforms = (identity, flip_y) 
  
  #Do upper LineMakers
  it = 0
  trans = transforms[it] 
  for i in range(mid):
    ii = mid - (i + 1)
    io = mid + (i + 2)
    Lx, Ly = io * LMdx, ii * LMdy
    buildLM()

  #Do lower LineMakers      
  it = 1
  trans = transforms[it] 
  for i in range(mid, bmheight):
    ii = i
    io = i + 2 
    Lx, Ly = io * LMdx, ii * LMdy + 158 
    buildLM()

  #Centre view over bitmap output area    
  golly.setpos(str(-pdx * bmwidth // 2 + (bmheight - 1) * LMdx), str(Ly//2))
  golly.setmag(-2)    #Aliasing effects happen at smaller scales than -2 :(
  #golly.fit()
          
def main():  
  #Vertical distance between pixels. Maybe get this from user.
  #minimum = 13 - LMsx%2; 18 seems to look best       
  pdy = 18 

  #Generate & display a dot matrix printer from current selection 
  dmprinter(pdy, copies=1)
  
  golly.setoption("hashing", True)
  golly.setbase(2)
  golly.setstep(6)  
  
main()
Last edited by PM 2Ring on September 3rd, 2009, 6:01 am, edited 1 time in total.
