# decode-Mateon-stdin-Golly4.py
# https://conwaylife.com/forums/viewtopic.php?p=125963#p125963
#
# Copy a Mateon stdin Catagolue hash value to the clipboard, then run this script.
#
# An example of a Mateon stdin soup can be found at this Catagolue link:
#   https://catagolue.hatsya.com/hashsoup/Mateon1_Glider6_5_6_Test/k_9HrHTiQjsT7V74016984/b3s23
# The RLE pattern shown there is nonsense. Instead it's necessary to feed the hash value --
#  k_iDjAk8wLX8Cv73216971
# -- into this script, to retrieve the actual pattern of gliders that produced the
# relevant census result for
#  https://catagolue.hatsya.com/object/xs35_651u0u156z0o5lkldzw11/b3s23
# (see the "Unofficial symmetries" section at the bottom of that census page).

import golly as g

import hashlib

def digest(bs):
    return hashlib.sha256(bs).digest()

hashval = bytes("\0" * 32, "ascii")
randcnt = 0
randbyte = 0
randbit = 0

def getRLE(seed):
    global randbit, randbyte, randcnt, hashval

    cells = set()

    hashval = digest(seed)
    randcnt = 0
    randbyte = 0
    randbit = 0

    def bit():
        global randbit, randbyte, randcnt, hashval
        if randbyte >= 32:
            assert randbit == 0
            randbyte = 0
            randcnt += 1
            hashval = digest(seed + bytes(":%d" % randcnt, "ascii"))

        val = (hashval[randbyte] >> randbit) & 1
        randbit += 1
        if randbit >= 8:
            randbit = 0
            randbyte += 1
        return val

    def rand(bits):
        assert bits <= 64
        val = 0
        for b in range(bits):
            val |= (1 << b) if bit() else 0
        return val

    PHASES = [
        [[1, 1, 1],
         [1, 0, 0],
         [0, 1, 0]],
        [[0, 1, 1],
         [1, 1, 0],
         [0, 0, 1]]]

    for quadrant in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        counter = 0
        while counter < glis:
            ori = bit()
            flip = bit()
            phase = bit()
            offs = rand(width)
            shift = rand(length) + 4
            (x, y) = (quadrant[0] * shift, quadrant[1] * shift)
            if ori:
                x += quadrant[0] * (offs + 1)
            else:
                y += quadrant[1] * offs
            r = 2
            bad = False
            for dx in range(-r, 3 + r):
                for dy in range(-r, 3 + r):
                    if (x + dx, y + dy) in cells:
                        bad = True
            if bad: continue
            for dy in range(3):
                for dx in range(3):
                    (gx, gy) = (2 - dx if quadrant[0] == -1 else dx, 2 - dy if quadrant[1] == -1 else dy)
                    (gx, gy) = (gy, gx) if flip else (gx, gy)
                    if PHASES[phase][gy][gx]:
                        cells.add((x + dx, y + dy))
            counter += 1

    xmin = min(x for (x, y) in cells)
    xmax = max(x for (x, y) in cells)
    ymin = min(y for (x, y) in cells)
    ymax = max(y for (x, y) in cells)

    rle = f"x = {xmax-xmin+1}, y = {ymax-ymin+1}, rule = {rule}\n"
    linerepeat = 0
    repeat = 0
    char = "b"
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            c = "o" if (x, y) in cells else "b"
            if c == char:
                repeat += 1
            else:
                if repeat and linerepeat:
                    if linerepeat > 1:
                    	rle+=str(linerepeat) + "$"
                    else:
                    	rle += "$"
                    linerepeat = 0
                if repeat:
                    if repeat > 1:
                        rle += str(repeat) + char
                    else:
                    	rle += char
                char = c
                repeat = 1
        if repeat and char != "b":
            if repeat > 1:
                rle += str(repeat) + char
            else:
            	rle += char
        repeat = 0
        linerepeat += 1
    rle += "!"
    return rle


# set this to the three values in the symmetry
(glis, width, length) = (6, 5, 6)
# and this to the rule
rule = "B3/S23"

#set this to the seed
seedstr = g.getclipstr()

# this was the previous sample, but it doesn't build anything interesting that I can recognize. (?)
# seedstr = "k_Nbke7qxLPRzS8441"

if seedstr[1] != "_":
  seedstr = g.getstring("Enter 18- or 22-character Catagolue seed for a Mateon stdin result: ","k_9HrHTiQjsT7V74016984")
seed = seedstr.encode()

g.new(seedstr)

# g.setclipstr(getRLE(seed))

rlestr = getRLE(seed)

pat = g.parse(rlestr.split("\n")[1])

g.putcells(pat)
g.fit()
