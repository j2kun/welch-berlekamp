#!/usr/bin/env python2.7

import numpy
from scipy import misc
from scipy import ndimage
from welchberlekamp import makeEncoderDecoder
import random

def corruptImage(message, numErrors):
   (numRows, numCols, numChannels) = message.shape
   indices = random.sample([(i,j) for i in range(numRows) for j in range(numCols)], numErrors)

   for i,j in indices:
      message[i][j][1] = random.randint(0,255)

   return message

def corrupt(message, numErrors):
   indices = random.sample(list(range(len(message))), numErrors)

   for i in indices:
      message[i][1] = random.randint(0,255)

   return message


def flatten(A):
   return numpy.array([entry for row in A for entry in row])


def vectorToImage(v, shape):
   numRows, numCols, numPixels = shape
   pixelVector = [v[i:i+3] for i in range(0, len(v), 3)]
   image = [pixelVector[i:i+numCols] for i in range(0, len(pixelVector), numCols)]
   return numpy.array(image)


def imageToVector(image):
   vector = flatten(flatten(image)) # each entry in the matrix is a 3-tuple (r,g,b)
   return vector


def imageTest():
   filename = "images/tiny-mars.jpg"
   image = ndimage.imread(filename)
   print("Loaded image")
   shape = (50, 50, 3)
   k = shape[0] * shape[1] * shape[2]
   n = 2 * k
   p = 16231
   e = 1000
   #p = 7387643

   print("Making encoder/decoder")
   enc, dec, solveSystem = makeEncoderDecoder(n, k, p)
   message = imageToVector(image)
   print("encoding the message")
   encoded = enc(message)

   print("corrupting the message")
   corrupted = corrupt(encoded[:], e)

   print("decoding the code")
   Q,E = solveSystem(corrupted)

   P, remainder = (Q.__divmod__(E))
   recoveredImage = vectorToImage([c.n for c in P.coefficients])
   misc.imsave("images/recovered-mars.jpg", recoveredImage)


def normalImageCorrupt():
   filename = "images/mars.jpg"
   image = ndimage.imread(filename)
   corrupted = corruptImage(image[:], 65536*8)
   misc.imsave("images/corrupted-mars.jpg", corrupted)

normalImageCorrupt()
