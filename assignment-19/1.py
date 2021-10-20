list = [ 1, 2, 3, 4 ,3, 2, 1]

shomarande = 0

for i in range (3):
   if list[i] == list[-1]:
       shomarande += 1
   list.pop()

if shomarande == 3:
    print('This list is symmetrical')
else:
    print("This list isn't symmetrical")