from music21 import *

a4 = note.Note("A4")
c4 = note.Note("C4")
rest = note.Rest()


wholeDuration = duration.Duration('whole')
dottedQuarter = duration.Duration(1.5)
eigthDuration = duration.Duration('eighth')
sixteenthDuration = duration.Duration('16th')

print(c4.pitch.frequency)
print(a4.pitch.frequency)

rest.show()

print(f"a dotted quarter note is equal to {dottedQuarter.quarterLength} quarter notes")
print(f"a sixteenth note is equal to {sixteenthDuration.quarterLength} quarter notes")
print(f"an eigth note is equal to {eigthDuration.quarterLength} quarter notes")