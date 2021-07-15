import golly as g
import os
libpath = g.getdir("data") + "recognizer-library/"
os.mkdir(libpath)

outfile = open(libpath+"splitter_weld2.rle", "w")
outfile.write("""#CXRLE Pos=-13,0
x = 35, y = 58, rule = B3/S23
13bo$12bobo$12bobo$13bo2$2o$bo$bobo$2b2o3$23b2o$23bo$21bobo$21b2o3$6bo
b2o$4b3ob2o$3bo$4b3ob2o$6bobo$6bobo$7bo$30b2o$25b2o2bo2bo$10b2o13bobo
2b2o$9bobo16b2o$9bo19bo$8b2o16bo2bob2o$25bobob2obo$26bobo$27bo2b2o$28b
2ob3o$34bo$13b2o13b2ob3o$13bo14b2obo$14bo$13b2o5b2o$12bo7b2o$12bo$11b
2obo$10bo2b2o$10b2o3$33b2o$33b2o5$18bo$17bobo$17bobo$18bo$15b3o$15bo!
""")

outfile = open(libpath+"splitter_welded.rle", "w")
outfile.write("""#CXRLE Pos=-7,0
x = 35, y = 63, rule = B3/S23
7b2o$7bo$7bo20b2o$7bobo18bo$8b2o16bobo$13bo12b2o$12bobo$12bobo$13bo2$
2o$bo$bobo$2b2o3$23b2o$23bo$21bobo$21b2o3$6bob2o$4b3ob2o$3bo$4b3ob2o$
6bobo$6bobo$7bo$30b2o$25b2o2bo2bo$10b2o13bobo2b2o$9bobo16b2o$9bo19bo$
8b2o16bo2bob2o$25bobob2obo$26bobo$27bo2b2o$28b2ob3o$34bo$28b2ob3o$28b
2obo2$20b2o$11b2o7b2o$12bo$12bobo$13b2o4$33b2o$33b2o5$18bo$17bobo$17bo
bo$18bo$15b3o$15bo!
""")

outfile = open(libpath+"splitter.rle", "w")
outfile.write("""#CXRLE Pos=-10,0
x = 62, y = 35, rule = B3/S23
10b2o11bo$10b2o10bobo$22bobo2b2o3bo$21b2ob2o2bo2bobo$25bobo3bobo$21b2o
bo2b4obo$21b2obobo3bo$25bobo3bo$26bobo3bo$27bo3b2o$46bo$44b3o$43bo$18b
2o23b2o$18b2o$3b2o$2bo2bo$bob2o$bo$2o$15b2o38b2o$15bo38bo2bo$16b3o36b
2o$18bo11b2o$31bo$28b3o6bob2o17b2o$28bo6b3ob2o17bo$34bo24b3o$35b3ob2o
20bo$37bobo$37bobo$38bo10b2o$49bo$50b3o$52bo!
""")

outfile = open(libpath+"A1_welded.rle", "w")
outfile.write("""x = 33, y = 60, rule = B3/S23
22bob2o$22b2obo$26b2o$28bo$28bo$26bob2o$26b2o2bo$29b2o4$32bo$8bo21b3o$
8b3o18bo$11bo17b2o$10b2o5$9b2o$8bobo$8bo$7b2o3$3b2o$2bo2bo2b2o$3b2o2bo
bo$5b2o16b2o$5bo17bo$2b2obo2bo15b3o$2bob2obobo16bo$6bobo$3b2o2bo$b3ob
2o$o$b3ob2o$3bob2o2$13b2o$13b2o7b2o$22bo$20bobo$20b2o4$2o$2o5$16bo$15b
obo$15bobo$16bo$17b3o$19bo!
""")

outfile = open(libpath+"A1.rle", "w")
outfile.write("""#CXRLE Pos=-28,0
x = 33, y = 57, rule = B3/S23
28b2o$28bo$26bobo$26b2o5$32bo$8bo21b3o$8b3o18bo$11bo17b2o$10b2o5$9b2o$
8bobo$8bo$7b2o3$3b2o$2bo2bo2b2o$3b2o2bobo$5b2o16b2o$5bo17bo$2b2obo2bo
15b3o$2bob2obobo16bo$6bobo$3b2o2bo$b3ob2o$o$b3ob2o$3bob2o2$13b2o$13b2o
7b2o$22bo$20bobo$20b2o4$2o$2o5$16bo$15bobo$15bobo$16bo$17b3o$19bo!
""")

outfile = open(libpath+"A2C4_weld3.rle", "w")
outfile.write("""#CXRLE Pos=-15,0
x = 33, y = 54, rule = B3/S23
15bo11bo$15b3o7b3o$18bo5bo$17b2o5b2o8$9b2o20b2o$9b2o20b2o8$3b2o$2bo2bo
2b2o$3b2o2bobo$5b2o16b2o$5bo17bo3bo$2b2obo2bo15b4o$2bob2obobo$6bobo$3b
2o2bo$b3ob2o$o$b3ob2o$3bob2o2$13b2o$13b2o7b2o$22bo$20bobo$20b2o4$2o$2o
5$16bo$15bobo$15bobo$16bo$17b3o$19bo!
""")

outfile = open(libpath+"A2C4_weld2.rle", "w")
outfile.write("""#CXRLE Pos=-15,0
x = 33, y = 58, rule = B3/S23
15bo11bo$15b3o7b3o$18bo5bo$17b2o5b2o8$9b2o20b2o$9b2o20b2o8$3b2o$2bo2bo
2b2o$3b2o2bobo$5b2o16b2o$5bo17bo$2b2obo2bo15b3o$2bob2obobo16bo$6bobo$
3b2o2bo$b3ob2o$o$b3ob2o$3bob2o2$13b2o$13b2o7b2o$22bo$20bobo$20b2o4$2o$
2o5$16bo$15bobo$15bob3o$16bo3bo$12b2o5bo$12bo2bo$14b2o$15bo$13bo$13b2o
!
""")

outfile = open(libpath+"A2C4_welded.rle", "w")
outfile.write("""#CXRLE Pos=-15,0
x = 33, y = 54, rule = B3/S23
15bo11bob2o$15b3o7b3ob2o$18bo5bo$17b2o5b2o8$9b2o20b2o$9b2o20b2o8$3b2o$
2bo2bo2b2o$3b2o2bobo$5b2o16b2o$5bo17bo$2b2obo2bo15b3o$2bob2obobo16bo$
6bobo$3b2o2bo$b3ob2o$o$b3ob2o$3bob2o2$13b2o$13b2o7b2o$22bo$20bobo$20b
2o4$2o$2o5$16bo$15bobo$15bobo$16bo$17b3o$19bo!
""")

outfile = open(libpath+"A2C4.rle", "w")
outfile.write("""#CXRLE Pos=-15,0
x = 33, y = 54, rule = B3/S23
15bo11bo$15b3o7b3o$18bo5bo$17b2o5b2o8$9b2o20b2o$9b2o20b2o8$3b2o$2bo2bo
2b2o$3b2o2bobo$5b2o16b2o$5bo17bo$2b2obo2bo15b3o$2bob2obobo16bo$6bobo$
3b2o2bo$b3ob2o$o$b3ob2o$3bob2o2$13b2o$13b2o7b2o$22bo$20bobo$20b2o4$2o$
2o5$16bo$15bobo$15bobo$16bo$17b3o$19bo!
""")

outfile = open(libpath+"B1.rle", "w")
outfile.write("""#CXRLE Pos=-52,0
x = 55, y = 68, rule = B3/S23
52bo$50b3o$49bo$49b2o3$33b2o14b2o$34bo14bobo$34bobo13bo$35b2o8$25bo$
23b3o$7bo14bo$7b3o12b2o$10bo$9b2o$53bo$52bobo$10b2o41b2o$10b2o4$30b2o$
30b2o3$3b2o37b2o$2bo2bo2b2o33bo$3b2o2bobo30b3o$5b2o16b2o15bo$5bo17bo$
2b2obo2bo15b3o$2bob2obobo16bo$6bobo$3b2o2bo$b3ob2o$o$b3ob2o$3bob2o2$
13b2o$13b2o7b2o$22bo$20bobo$20b2o4$2o$2o5$16bo$15bobo$15bobo$16bo$17b
3o$19bo!
""")

outfile = open(libpath+"B2_welded.rle", "w")
outfile.write("""#CXRLE Pos=-41,0
x = 77, y = 33, rule = B3/S23
41b2o$33bo7b2o31b2o$33b3o38bobo$36bo38b2o$35b2o2$27b2o$28bo$28bobo$18b
o10b2o$16b3o$15bo57b2o$2bo12b2o56bo$3bo70b3o$3bo72bo$2ob2o$obo2bo$3b2o
$18b2o$18b2o31b2o$52bo$41b2o6b3o$41b2o2b2o2bo$27bo3b2o12bobobo$26bobo
3bo14bob2o$25bobo3bo15bo$21b2obobo3bo15b2o$21b2obo2b4obo$25bobo3bobo$
21b2ob2o2bo2bobo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo!
""")

outfile = open(libpath+"B2.rle", "w")
outfile.write("""#CXRLE Pos=-18,0
x = 33, y = 77, rule = B3/S23
18b2o9b2o$19bo9bobo$19bobo8b2o$20b2o21$12b2o$11bobo$8bo2bo$8b4o2$6b4o$
6bo3bo$9b2o3$10b2o19b2o$10b2o19b2o5$28b2o$28bobo$30bo$3b2o25b2o$2bo2bo
2b2o$3b2o2bobo$5b2o16b2o$5bo17bo$2b2obo2bo15b3o$2bob2obobo16bo$6bobo$
3b2o2bo$b3ob2o$o$b3ob2o$3bob2o2$13b2o$13b2o7b2o$22bo$20bobo$20b2o4$2o$
2o5$16bo$15bobo$15bobo$16bo$17b3o$19bo!
""")

outfile = open(libpath+"C1_welded.rle", "w")
outfile.write("""x = 38, y = 30, rule = B3/S23
33b2o$33bo$35bo$13bob2o14b5o$10b2obo2bo13bo$10b2ob2obobo12b3o$15bob2o
15bo$15bo15b4o$13b3o10b2o3bo3b2o$12bo13b2o4b3o2bo$12b2o20bob2o$34bo$
33b2o3$25b2o$25bo$2b2o22b3o$bobo5b2o17bo$bo7b2o$2o2$14bo$10b2obobo$9bo
bobobo$6bo2bobobobob2o$6b4ob2o2bo2bo$10bo4b2o$8bobo$8b2o!
maxticks = 1""")

outfile = open(libpath+"C1.rle", "w")
outfile.write("""#CXRLE Pos=-33,0
x = 38, y = 30, rule = B3/S23
33b2o$33bo$35bo$15b2o14b5o$13bo2bo13bo$13b2obobo12b3o$15bob2o15bo$15bo
15b4o$13b3o10b2o3bo3b2o$12bo13b2o4b3o2bo$12b2o20bob2o$34bo$33b2o3$25b
2o$25bo$2b2o22b3o$bobo5b2o17bo$bo7b2o$2o2$14bo$10b2obobo$9bobobobo$6bo
2bobobobob2o$6b4ob2o2bo2bo$10bo4b2o$8bobo$8b2o!
""")

outfile = open(libpath+"C2_welded.rle", "w")
outfile.write("""#CXRLE Pos=-26,0
x = 51, y = 27, rule = B3/S23
26b2o$27bo$27bobo$17bo10b2o$15b3o$14bo$2o12b2o$o48b2o$o48b2o$ob2o$bo2b
o$2b2o$17b2o$17b2o4$26bo3b2o$25bobo3bo$24bobo3bo$20b2obobo3bo$20b2obo
2b4obo$24bobo3bobo6b2o$20b2ob2o2bo2bobo6b2o$21bobo2b2o3bo$9b2o10bobo$
9b2o11bo!
""")

outfile = open(libpath+"C2.rle", "w")
outfile.write("""#CXRLE Pos=-27,0
x = 52, y = 27, rule = B3/S23
27b2o$28bo$28bobo$18bo10b2o$16b3o$15bo$15b2o$2o48b2o$bo48b2o$bob2o$2bo
2bo$3b2o$18b2o$18b2o4$27bo3b2o$26bobo3bo$25bobo3bo$21b2obobo3bo$21b2ob
o2b4obo$25bobo3bobo6b2o$21b2ob2o2bo2bobo6b2o$22bobo2b2o3bo$10b2o10bobo
$10b2o11bo!
""")

outfile = open(libpath+"C3.rle", "w")
outfile.write("""#CXRLE Pos=-52,0
x = 56, y = 35, rule = B3/S23
52b2o$52bo$50bobo$33b2o15b2o$34bo$34bobo17bo$35b2o15b3o$51bo$27b2o22b
2o$28bo$28bobo$18bo10b2o$16b3o$15bo36b2o$15b2o35bobo$2o52bo$bo52b2o$bo
b2o$2bo2bo$3b2o$18b2o$18b2o2$41b2o$41b2o2b2o$27bo3b2o12bobo$26bobo3bo
14bo$25bobo3bo15b2o$21b2obobo3bo$21b2obo2b4obo$25bobo3bobo$21b2ob2o2bo
2bobo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo!
""")

outfile = open(libpath+"D1.rle", "w")
outfile.write("""x = 39, y = 82, rule = B3/S23
2o$bo$bobo$2b2o7$b2o4b2o$b2o4b2o4$6b2o$2b2o2b2o$bobo$bo12b2o$2o11bobo$
13bo$12b2o5$14b2o$13bobo$13bo$12b2o$11bo$11b3o$14bo$13b2o6$11b2o$11b2o
$35b2o$35bobo$37bo$37b2o4$11b2o$10bo2bo2b2o$11b2o2bobo$13b2o$13bo$10b
2obo2bo$10bob2obobo$14bobo$11b2o2bo$9b3ob2o$8bo$9b3ob2o$11bob2o2$21b2o
$21b2o7b2o$30bo$28bobo$28b2o4$8b2o$8b2o5$24bo$23bobo$23bobo$24bo$25b3o
$27bo!""")

outfile = open(libpath+"D2_welded.rle", "w")
outfile.write("""#CXRLE Pos=-15,0
x = 33, y = 53, rule = B3/S23
15bo11bo$15b3o7b3o$18bo5bo$17b2o5b2o8$9b2o20b2o$9b2o20b2o8$3b2o$2bo2bo
2b2o$3b2o2bobo$5b2o16b2o$5bo17bo$2b2obo2bo15b3o$2bob2obobo16bo$6bobo$
3b2o2bo$b3ob2o$o$b3ob2o$3bob2o2$13b2o$13b2o7b2o$22bo$20bobo$20b2o4$2o$
2o5$16bo$15bobo$15bobo$16bo3bo$17b4o!
""")

outfile = open(libpath+"D2.rle", "w")
outfile.write("""#CXRLE Pos=-41,0
x = 54, y = 33, rule = B3/S23
41b2o$41b2o4$52b2o$27b2o23bo$28bo21bobo$28bobo19b2o$18bo10b2o$16b3o$
15bo$15b2o$2o$bo48b2o$bob2o45bobo$2bo2bo46bo$3b2o47b2o$18b2o$18b2o3$
41b2o$27bo3b2o8b2o$26bobo3bo$25bobo3bo$21b2obobo3bo$21b2obo2b4obo$25bo
bo3bobo$21b2ob2o2bo2bobo$22bobo2b2o3bo$10b2o10bobo$10b2o11bo!
""")

outfile = open(libpath+"weld_m.rle", "w")
outfile.write("""#CXRLE Pos=-89,0
x = 108, y = 56, rule = B3/S23
89bo$78b2o7b3o$73bo5bo6bo$73b3o3bobo4b2o$76bo3b2o$75b2o2$100bo$98b3o$
97bo$97b2o$34b2o$b2o31b2o7bo$obo38b3o52b2o$2o38bo55b2o$40b2o2$48b2o$
48bo$46bobo29b2o$46b2o10bo20bo$58b3o15b3o$2b2o57bo14bo26b2o$3bo56b2o
12bobo21b2o2bo2bo$3o70bobo22bobo2b2o$o72bobobo2bo2b2o16b2o$72b2obob4o
3bo17bo$71bo2bo6b3o15bo2bob2o$72b2o5bo2bo15bobob2obo$57b2o20b2o3bo14bo
bo$24b2o31b2o24b2o15bo2b2o$24bo76b2ob3o$25b3o6b2o71bo$27bo2b2o2b2o65b
2ob3o$27bobobo12b2o3bo51b2obo$26b2obo14bo3bobo$29bo15bo3bobo41b2o$29b
2o15bo3bobob2o28b2o7b2o$44bob4o2bob2o29bo$43bobo3bobo33bobo$43bobo2bo
2b2ob2o30b2o$44bo3b2o2bobo$52bobo10b2o$53bo11b2o$106b2o$106b2o5$91bo$
90bobo$90bobo$91bo$88b3o$88bo!
""")

outfile = open(libpath+"snark.rle", "w")
outfile.write("""#CXRLE Pos=-9,0
x = 19, y = 23, rule = B3/S23
9b2o$8bobo$2b2o4bo$o2bo2b2ob4o$2obobobobo2bo$3bobobobo$3bobob2o$4bo2$
17b2o$8b2o7bo$8b2o5bobo$15b2o7$5b2o$6bo$3b3o$3bo!
""")

outfile = open(libpath+"snark_v2.rle", "w")
outfile.write("""#CXRLE Pos=-13,0
x = 23, y = 19, rule = B3/S23
13bo$11b3o$10bo$10b2o3$18b2o$19bo$19bob2o$11b2o4b3o2bo$11b2o3bo3b2o$
16b4o$2b2o15bo$bobo12b3o$bo13bo$2o14b5o$20bo$16b2o$16b2o!
""")

outfile = open(libpath+"snark_welded.rle", "w")
outfile.write("""#CXRLE Pos=-2,0
x = 19, y = 22, rule = B3/S23
2b4o$2bo3bo$5b2o7$15b2o$8b2o5bobo$8b2o7bo$17b2o2$4bo$3bobob2o$3bobobob
o$2obobobobo2bo$o2bo2b2ob4o$2b2o4bo$8bobo$9b2o!
""")

outfile = open(libpath+"rectifier.rle", "w")
outfile.write("""#CXRLE Pos=-25,0
x = 33, y = 41, rule = B3/S23
25bob2o$25b2obo2$23b5o$23bo4bo2b2o$26bo2bo2bo$26b2obobo$23bo5bob2o$22b
obo4bo$22bo2bo2b2o$23b2o9$15b2o$15b2o8$b2o22b2o$o2bo21bo$b2o23b3o$28bo
6$18b2o$18bo$19b3o$21bo!
""")

outfile = open(libpath+"weekender_to_glider.rle", "w")
outfile.write("""#CXRLE Pos=-18,0
x = 32, y = 118, rule = B3/S23
18bo$16b3o$15bo$2o13b2o$2o5$25bo$23b3o$22bo$22b2o$2o$2o6$12b2o$12b2o$
26b2o$26b2o$30b2o$30b2o14$6b2o$6bobo$7bo12$25bo$23b3o$22bo$22b2o7$27b
2o$27bo$25bobo$25b2o3$11b2o$10bobo$10bo$9b2o3$27b2obo$27bob2o2$20b2o$
20b2o14$31bo$29b3o$28bo$28b2o10$8b2o$8b2o9$23b2o$23b2o!
""")

outfile = open(libpath+"eater.rle", "w")
outfile.write("""#CXRLE Pos=-2,0
x = 4, y = 4, rule = B3/S23
2b2o$bobo$bo$2o!
""")

outfile = open(libpath+"glider.rle", "w")
outfile.write("""#CXRLE Pos=0,0
x = 3, y = 3, rule = B3/S23
2o$b2o$o!
maxticks = 1""")

outfile = open(libpath+"library.txt", "w")
outfile.write("""splitter_weld2
splitter_welded
splitter
A1_welded
A1
A2C4_weld3
A2C4_weld2
A2C4_welded
A2C4
B1
B2_welded
B2
C1_welded
C1
C2_welded
C2
C3
D1
D2_welded
D2
weld_m
snark
snark_v2
snark_welded
rectifier
weekender_to_glider
eater
glider
""")

outfile.close()
g.exit("Created library in "+libpath[:-1]+".")