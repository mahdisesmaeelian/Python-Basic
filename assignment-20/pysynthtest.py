import pysynth_b
import play_wav

# (('g', 4), ('g', 4), ('c6', 2),('g',4), ('g', 4), ('c6', 2))
my_string = eval(input())

pysynth_b.make_wav(my_string, fn = "test.wav")

play_wav.Sound().playFile('test.wav')
