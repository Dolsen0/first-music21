from music21 import *
a4 = note.Note("A4")
c4 = note.Note("C4")
rest = note.Rest()


print(c4.pitch.frequency)
print(a4.pitch.frequency)

rest.show()