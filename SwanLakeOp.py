from music21 import note, stream, tempo
notes = ['B', 'E', 'F#', 'G', 'A', 'B', 'G', 'B', 'G', 'B', 'E', 'G', 'E', 'C', 'G', 'F#', 'B', 'E', 'F#', 'G', 'A']
st = stream.Stream()


for n in notes:
  new_note = note.Note(n)
  st.append(new_note)

for i in range (0):
  st[i].duration.quarterLength = 2

for i in range (4):
  st[i].duration.quarterLength = 8

for i in range (5):
  st[i].duration.quarterLength = 4

for i in range (6):
  st[i].duration.quarterLength = 8

for i in range (7):
  st[i].duration.quarterLength = 4

for i in range (8):
  st[i].duration.quarterLength = 8

for i in range (9):
  st[i].duration.quarterLength = 4

for i in range (15):
  st[i].duration.quarterLength = 8

for i in range (16):
  st[i].duration.quarterLength = 2

for i in range (20):
  st[i].duration.quarterLength = 8

st.insert(0,tempo.MetronomeMark(number=180))

st.write('midi', fp="swanlake.mid")