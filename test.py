""" Example of sending data to Aptgraph using Python """
from pyaptgraph import *
import random

# Get a instance of the API (this is YOUR apikey)
api = PyAptgraph('wKJtkVq3QXoUJW5hryrFXRXDEoJhiwFmvA2KEWMSNH3AcMMPsx')

# Add a couple of random values to this graph (8jspy is this graphs id) then send it to Aptgraph
api.add('8jspy', random.randint(1,100))
api.add('8jspy', random.randint(1,100))
api.send()
