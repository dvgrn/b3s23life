# ticker-tape-maker-p30.py
# Golly Python script. Written by PM 2Ring, March 2009. Updated August 2009.
# Modified for Golly 2.0+ by Andrew Trevorrow.
# Updated to Python3 by Dave Greene, June 2022.

''' Create a 'bitmap printer'.

    Print a bitmap in LWSSs, using the current selection as the bitmap source.
'''

import golly
from glife import *

def get_bitmap():
    ''' Get current selection & turn it into a bitmap. '''
    selrect = golly.getselrect()
    if len(selrect) == 0: golly.exit("There is no selection, aborting.")

    #Get bitmap size
    w, h = selrect[2:]
    #Adjust width, so it's in the form of 4m, m>1
    w = (w + 3) // 4 * 4
    w = max(8, w)

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

def linemaker(loopm):
    ''' Create an empty LineMaker '''
    LM = pattern('''
34b2o$34bo$25b2o5bobo$24b3o5b2o$12bo8bob2o$12bobo6bo2bo$2o11bobo5bob2o
$2o11bo2bo7b3o21b2o$13bobo9b2o21b2o$12bobo$12bo9bo$23b2o$22b2o6$47b3o$
24b2o20bo3bo$24b2o19bo5bo$46bo3bo$47b3o$47b3o5$49b3o$44bo3b2ob2o$42b2o
4b2ob2o$35b2o6b2o3b5o$35b2o10b2o3b2o7$45b2o5b2o$45bo6bo$46b3o4b3o$48bo
6bo!''')
    LMTop = LM + pattern('2b2o$2bo$obo$2o!', 32, 7)
    LMBase = pattern('''
11bo$10bo$10b3o12$23b2o$23bobo$10bobo13bo$9bo2bo2b2o6bo2bo12b2o$8b2o5b
obo8bo11b3o$2o4b2o3bo3bo3bo3bobo9bob2o15bo$2o6b2o5b3ob2o2b2o10bo2bo8b
3o4bobo$9bo2bo3b2o17bob2o16bobo$10bobo25b3o2b2o2bo7bo2bo3b2o$39b2o2bo
3bo7bobo4b2o$44bo2bo6bobo$26bo17b2o8bo$24bobo$25b2o2$36bo$36bobo$36b2o
7$33bo7bo$32b4o5bobo$27b2o2bo2b2o8b2o4b2o$27b2o2b2o11b2o4b2o$16b2o6b2o
10bo7b2o$16b2o5b3o10bo4bobo$24b2o10bo4bo$27b2o$27b2o!''', 14, 29)
    LMBase += LM(55, 42, flip) 
    return LMTop(8 + loopm, -21 - loopm) + LMBase

def dmprinter(pdy, copies=1):
    ''' Generate & display a dot matrix printer for named bitmap pattern '''
    #Horizontal pixel separation between LineMakers. minimum = 5
    LMsx = 5

    #Horizontal distance between bitmap pixels. Constant, due to LineMaker period
    pdx = 15

    #Distance between LineMakers
    LMdx, LMdy = -LMsx * pdx, pdy

    #Get bitmap pattern from current selection.
    bm = get_bitmap()

    #Make printer in a new layer
    golly.duplicate()
    golly.setoption("syncviews", False)

    #Build new window title from old
    title = golly.getname().split('.')[0]
    title = '%s_Printer [%d] v0.10' % (title, pdy)
    golly.new(title)

    #Make sure we're using the standard Life generation rule
    golly.setrule("B3/S23")

    #Bitmap dimensions. Width MUST be of form 4m, for m >=1
    bmheight = len(bm)
    bmwidth = len(bm[0])
    mid = (bmheight + 1) // 2

    loopw = (bmwidth - 8) // 4
    loopm = pdx * loopw

    #Gliders, heading north-east
    g0 = pattern('2bo$2o$b2o!')
    g1 = pattern('obo$2o$bo!')
    gliders = [g0, g1, g1(0, 2, rccw), g0(0, 2, rccw),
        g0(2, 2, flip), g1(2, 2, flip), g1(2, 0, rcw), g0(2, 0, rcw)]
        
    #Create full Glider loop.
    gg = []
    ox, oy = 35, 23
    for j in range(loopw + 1):
        dd = pdx * j
        gg += [gliders[0](ox + dd, oy - dd), gliders[1](ox + 8 + dd, oy - 7 - dd)]
    dd = loopm
    gg += [gliders[2](45 + dd, 4 - dd), gliders[3](37 + dd, -3 - dd)]

    ox, oy = 26 + loopm, -4 - loopm
    for j in range(loopw + 1):
        dd = pdx * j
        gg += [gliders[4](ox - dd, oy + dd), gliders[5](ox - 8 - dd, oy + 7 + dd)]
    dd = loopm
    gg += [gliders[6](16, 15), gliders[7](24, 22)]
    parity = 2*((loopw + 1)*(0, 0) + (1, 1))

    def buildLM():
        ''' Build a complete LineMaker '''
        #Populate glider loop. (jj, ii) are bitmap coords
        gloop = pattern()
        for j in range(bmwidth):
            jj = (j - delta + bmwidth - 1) % bmwidth

            #Is there a pixel at this location?
            if bm[ii][jj] == parity[j]:                
                gloop += gg[j]  #Add glider to the loop

        #Only put LineMaker if glider loop isn't empty
        if len(gloop) > 0:
            (LMBlank + gloop).put(Lx, Ly, trans)

    #Assemble blank LineMaker
    LMBlank = linemaker(loopm)

    #Do upper LineMakers
    trans = identity
    for i in range(mid):
        ii = mid - (i + 1)
        io = mid + (i + 1)
        Lx, Ly = io * LMdx, ii * LMdy
        delta = LMsx * io
        buildLM()

    #Do lower LineMakers
    trans = flip_y
    for i in range(mid, bmheight):
        ii = i
        io = i + 2
        Lx, Ly = io * LMdx + pdx, ii * LMdy + 128
        delta = LMsx * io - 1
        buildLM()

    #Eaters facing south-east & north-east
    eaterSE = pattern('2o$bo$bobo$2b2o!')
    eaterNE = eaterSE(0, 10, flip_y)
    eY = 59
    eaters = (eaterNE(0, eY), eaterSE(0, eY))
    
    #Eater horizontal displacement. Must be odd
    #bmwidth muliplier determines number of copies visible 'outside' printer.
    eX = (bmheight + 1) * LMdx - (copies * bmwidth - 1) * pdx   
    eX = 1 + eX // 2 * 2    #Adjust parity
    all = pattern()
    for i in range(bmheight):
        all += eaters[i % (1 + LMsx % 2)](eX, i * LMdy)
    all.put()   

    #Centre view over bitmap output area
    golly.setpos(str(-pdx * bmwidth // 2 + (bmheight - 1) * LMdx), str(Ly//2))
    #golly.setmag(-2)    #Aliasing effects happen at smaller scales than -2 :(
    golly.fit()

def main():
    #Vertical distance between pixels. Maybe get this from user. minimum = 16
    pdy = 16

    #Generate & display a dot matrix printer from current selection
    dmprinter(pdy, copies=1)

    golly.setcursor("Zoom In")
    golly.setalgo("HashLife")
    golly.setbase(2)
    golly.setstep(6)

main()
