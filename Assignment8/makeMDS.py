
#!/usr/local/bin/python

# all code here stolen shamelessly from 
# "Programming Collective Intelligence, Chapter 3"

import sys

sys.path.insert(0, '../libs')

import clusters

blognames,words,data=clusters.readfile('data.txt')

coords = clusters.scaledown(data)

clusters.draw2d(coords, blognames, jpeg='MDS.jpg')