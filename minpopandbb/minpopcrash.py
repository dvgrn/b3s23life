# minpopcrash.py

# no clever calculations of relevant area here, just hard-coded numbers to change for different spaceships
import golly as g

pat1 = g.parse("""29bobo$29b2o$30bo8bo$11bo25b2o$9bobo26b2o$10b2o4$22bobo7bo$5bobo14b2o
8bobo$6b2o4bo10bo8b2o$6bo3bobo$11b2o$2bo$obo20bo$b2o19bobo$21bob2o$21b
o$20b2o14bo$13b2o20b2o$11b3obob2o16bobo$10bo4bobo$10b6o2b3o$16b2o3bo$
10b6o2b3o$10bo4bobo$11b3obob2o$13b2o$20b2o7bo$21bo7bobo$21bob2o4b2o$b
2o19bobo$obo20bo$2bo28b3o$11b2o18bo$6bo3bobo19bo$6b2o4bo10bo$5bobo14b
2o$22bobo4$10b2o$9bobo$11bo$30bo$29b2o$29bobo!""")
pat2 = g.parse("""11bo$12b2o42bobo$11b2o15bo27b2o$26bobo16bo11bo$27b2o15bo$16bo27b3o$9bo
4bobo$10b2o3b2o$9b2o41bo6bobo$50b2o7b2o$7bo43b2o7bo$5bobo$6b2o5bo$14bo
$12b3o$26b2o4b2o$26bo4bo2bo$17bo9bo3bo2bo7b3o$2bo15b2o8bo3b2o$obo14b2o
10bo$b2o27bo5bo$9bo21bo5b2o$7bobo16b2o2b2o3b2o$8b2o16b2o2bo6bo$31bo8bo
$30b2o7bobo$29bo9bobo$29bob3o6bo8b2o$30bobobo14bobo$34bo14bo$26bo7b2o
25bo2bo$24bobo33bo$25bobo32bo3bo$25bo34b4o$29b2o5bo$28bo2bo3bobo$7b2o
20b2o4bobo$6bobo12bo14bo$8bo12bo$21bo28bo$49b2o$49bobo5b2o$2b2o52b2o$b
obo54bo$3bo28b2o$32bobo18bo7b3o$12b2o18bo19b2o7bo$13b2o37bobo7bo$12bo
22b3o$21b2o12bo$20bobo13bo19b3o$5bo16bo33bo$5b2o19b3o28bo$4bobo21bo$
12bo14bo$12b2o$11bobo!""",58,0)

g.setalgo("QuickLife")
g.setrule("Life")

count, minpop, minpat = 0, 999999, []
for t in range(4):
  for x in range(-10,10):
    for y in range(-20,40):
      g.new("Test " + str(count))
      count += 1
      g.putcells(pat1)
      g.putcells(pat2,x,y)
      pat = g.getcells(g.getrect())
      g.run(16384)
      pop = int(g.getpop())
      if pop<minpop:
        minpop = pop
        minpat = pat
      g.show(str([count,t,x,y,pop,minpop]))
  pat2 = g.evolve(pat2,1)
g.new("Lowest pop collision")
g.putcells(minpat)
