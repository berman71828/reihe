indices = [0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11]

pitches = ['c','cs','db','d','ds','eb','e','f','fs','gb','g','gs','ab','a','as','bb','b']

preferred_pitch_name = dict([('db','cs'), ('ds','eb'), ('gb','fs'), ('gs','ab'), ('as','bb')])

def getPitchClass (pitchName):
  i = pitches.index(pitchName)
  return indices[i]

def normalize (row):
  diff = 12 - row[0]
  baseline_row = []
  for position in range (0, 12):
    baseline_row.append((row[position] + diff) % 12)
  print baseline_row

def getPitchName (pitchNumber):
  num = pitchNumber % 12
  index = indices.index(num)
  # try:
  try:
    pitchName = preferred_pitch_name[pitches[index]] 
  except KeyError:
    pitchName = pitches[index]
  return pitchName

def getPitchNames (row):
  pitchNames = [] 
  for position in range (0, 12):
    pitchNames.append( getPitchName(row[position]) )
  return pitchNames

def transpose (originalRow, delta):
  transposedRow = []
  for position in range (0, 12):
    transposedRow.append( (originalRow[position] + delta) % 12 )
  return transposedRow

def printAllTranspositions (originalRow):
  for delta in range (0, 12):
    print getPitchNames( transpose(originalRow, delta) )
    print transpose(originalRow, delta) 
    print " "
    print " "
