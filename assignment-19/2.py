import random

boys = ['ali', 'matin', 'mohsen','iman', 'amin', 'behnam', 'avash', 'babak']
girls = ['sogand', 'zahra', 'sima', 'elham', 'mahsa', 'elahe', 'sahar', 'mobina']
result = []
random.shuffle(boys)
random.shuffle(girls)

for i in range(len(boys)):
    result.append('('+boys[i]+','+girls[i]+')')

print(result)