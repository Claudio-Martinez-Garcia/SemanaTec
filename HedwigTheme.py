from music21 import note, stream, tempo
notes = ['B', 'E2', 'G4', 'F#3', 'E2', 'B5', 'A4', 'F#2', 'E1', 'G4', 'F#3', 'Eb2', 'F3', 'B', 'B', 'E5', 'G4', 'F#', 'E3', 'B', 'D5', 'Db4', 'C1', 'Ab', 'C', 'B', 'Bb', 'Bb2', 'G4', 'E']
st = stream.Stream()

for n in notes:
  new_note = note.Note(n)
  st.append(new_note)

for i in range (1):
  st[i].duration.quarterLength = 4

for i in range (2):
  st[i].duration.quarterLength = 8

for i in range (3):
  st[i].duration.quarterLength = 4

for i in range (4):
  st[i].duration.quarterLength = 2

for i in range (5):
  st[i].duration.quarterLength = 4

for i in range (7):
  st[i].duration.quarterLength = 2

for i in range (8):
  st[i].duration.quarterLength = 4

for i in range (9):
  st[i].duration.quarterLength = 8

for i in range (10):
  st[i].duration.quarterLength = 4

for i in range (11):
  st[i].duration.quarterLength = 2

for i in range (12):
  st[i].duration.quarterLength = 4

for i in range (13):
  st[i].duration.quarterLength = 2

for i in range (14):
  st[i].duration.quarterLength = 4

for i in range (29):
  st[i].duration.quarterLength = 4


st.insert(0,tempo.MetronomeMark(number=150))

st.write('midi', fp="hedwigtheme.mid")