# minimal code for oscillators (only) --
# can be faster than an equivalent oscar.py/.lua run (I think)
# and can also be arranged to run in parallel, if some copies of the
# unknown pattern are advanced with HashLife, then checked for a hash match
# from that point.
import golly as g

h = g.hash([-608,-609,1220,1220])
newhash = 0
count = 0

while newhash != h:
  g.run(1)
  count += 1
  newhash = g.hash([-608,-609,1220,1220])
  if count%100 == 0:
     g.show(str([count,h,newhash]))
