
from reedsolomon import makeEncoderDecoder
import random

def simpleTest():
   integerMessage = [2,3,2]
   k = 3
   n = 7
   p = 11

   enc, dec, solveSystem = makeEncoderDecoder(n, k, p)
   encoded = enc(integerMessage)

   print("plain message is: %r" % (integerMessage,))
   print("encoded message is: %r" % (encoded,)) # cleaner output

   e=1
   corrupted = encoded[:]
   corrupted[n//2][1] = corrupted[n//2][1] + 1
   print("corrupted message is: %r" % (corrupted,))

   Q,E = solveSystem(corrupted)
   P, remainder = (Q.__divmod__(E))

   print("P(x) = %r" % P)
   print("r(x) = %r" % remainder)


def corrupt(message, numErrors, minVal=0, maxVal=131):
   indices = random.sample(list(range(len(message))), numErrors)

   for i in indices:
      message[i][1] = random.randint(minVal, maxVal)

   return message


def tkamTest():
   message = '''When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh. He couldn't have cared less, so long as he could pass and punt.

When enough years had gone by to enable us to look back on them, we sometimes discussed the events leading to his accident. I maintain that the Ewells started it all, but Jem, who was four years my senior, said it started long before that. He said it began the summer Dill came to us, when Dill first gave us the idea of making Boo Radley come out.'''

   k = len(message)
   n = len(message) * 2
   p = 2087
   integerMessage = [ord(x) for x in message]

   enc, dec, solveSystem = makeEncoderDecoder(n, k, p)
   print("encoding...")
   encoded = enc(integerMessage)

   e = int(k/2)
   print("corrupting...")
   corrupted = corrupt(encoded[:], e, 0, p)

   print("decoding...")
   Q,E = solveSystem(corrupted)
   P, remainder = (Q.__divmod__(E))

   recovered = [chr(x) for x in P.coefficients]
   print(recovered)

tkamTest()
