 import pysynth_b

def write(self, melody,title,times=None):
     abc_notation = []
     for i in range(len(melody)):
         if isinstance(melody[i],tuple):
             note = melody[i][0]
             note_time = melody[i][1]
         else:
             note = melody[i]
             if times:
                 note_time = times[i]
                 if note_time == 0:
                     note_time = 4
             else:
                 note_time = 4
         abc_notation.append((self.number_to_abc(note),note_time))
     print("ABC to write:",abc_notation)
     pysynth_b.make_wav(abc_notation,fn=title)