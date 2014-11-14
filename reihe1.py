indices = [0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11]
pitches = ['c','cs','db','d','ds','eb','e','f','fs','gb','g','gs','ab','a','as','bb','b']

def getPitchClass (pitchName):
  i = pitches.index(pitchName)
  return indices[i]


