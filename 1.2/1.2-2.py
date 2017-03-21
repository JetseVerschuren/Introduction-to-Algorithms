import math

for n in range(1,500):
    insertion = 8*n**2
    merge = 64*n*math.log(n)
    if insertion < merge:
        print "beat id: " + str(n) + " insertion: " + str(insertion) + " merge: " + str(merge)
    else:
        print "not-beat id: " + str(n) + " insertion: " + str(insertion) + " merge: " + str(merge)
