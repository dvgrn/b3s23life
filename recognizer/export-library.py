import golly as g
import hashlib
import os

libpath = g.getdir("data") + "recognizer-library/"
libraryFN = libpath + "library.txt"

def removecomments(s):
   temp = s + "#"
   return temp[:temp.find("#")].rstrip()

f = open(libraryFN, 'r')
patnames=f.readlines()
f.close()
patnames+=["library"] # export the library file, too

output_script_filename = g.getdir("scripts")+"populate-sample-library.py"
outfile = open(output_script_filename,"w")

outfile.write('import golly as g\nimport os\nlibpath = g.getdir("data") + "recognizer-library/"\n')
outfile.write('os.mkdir(libpath)\n\n')

for name in patnames:
   basename = removecomments(name)
   if basename=="library":
     realname=basename+".txt"
   else:
     realname=basename+".rle"
   temp = basename.split(" ")
   if len(temp)==2: basename, tickstorun = temp
   if len(temp)==3: basename, tickstorun, matchtype = temp
   p = open(libpath + realname,"r")
   s=p.read()
   outfile.write('outfile = open(libpath+"'+realname+'", "w")\noutfile.write("""'+s+'""")\n\n')

outfile.write('outfile.close()\ng.exit("Created library in "+libpath[:-1]+".")')
outfile.close()

g.exit("Created "+ output_script_filename + ".")